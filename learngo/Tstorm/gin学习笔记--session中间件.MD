gin学习笔记--session中间件
目录

cookie和session基础知识点总结
Cookie
Session
源码展示
目录结构
源码
预期效果
重点总结
 

gin学习笔记--session中间件
回到顶部
cookie和session基础知识点总结
Cookie
HTTP请求是无状态的，

服务端让用户的客户端（浏览器）保存一小段数据

Cookie作用机制:
是由服务端保存在客户端的键值对数据（客户端可以阻止服务端保存Cookie）

每次客户端发请求的时候会自动携带该域名下的Cookie

不用域名间的Cookie是不能共享的

Go操作Cookie:
net/http

查询Cookie:http.Cookie("key")

设置Cookie:·http.SetCookie(w http.ResponseWriter, cookie *http.Cookie)

gin框架操作Cookie:
查询Cookie：c.Cookie("key")

设置Cookie:c.SetCookie("key", "value", domain, path, maxAge, secure, httpOnly)

Cookie的应用场景
保存HTTP请求的状态

保存用户登录的状态
保存用户购物车的状态
保存用于定制化的需求
Cookie的缺点：
数据量最大4K
保存在客户端（浏览器）端，不安全
Session
保存在服务端的键值对数据。

Session的存在必须依赖于Cookie,Cookie中保存了每个用户Session的唯一标识。

Session的特点：
保存服务端，数据量可以存很大（只要服务器支持）
保存在服务端也相对保存在客户端更安全
需要自己去维护一个Session服务，会提高系统的复杂度。
Seesion的工作流程
mark

回到顶部
源码展示
目录结构
mark

源码
main.go

package main

//gin demo
import (
	"github.com/gin-gonic/gin"
	"github.com/gin_learing/session/gin_session"
	"net/http"
)

func main(){
	r:=gin.Default()
	r.LoadHTMLGlob("templates/*")
	//初始化全局的mgrobj
	gin_session.InitMgr("redis","127.0.0.1:6379")
	//session作为全局的中间件
	r.Use(gin_session.SessionMiddleware(gin_session.MgrObj))
	r.Any("/login", loginHandler)
	r.GET("/index", indexHandler)
	r.GET("/home", homeHandler)
	r.GET("/vip", AuthMiddleware, vipHandler)

	//没有匹配到走下面
	r.NoRoute(func(c *gin.Context) {
		c.HTML(http.StatusNotFound, "404.html", nil)
	})
	r.Run()
}
handler.go

package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/gin_learing/session/gin_session"
	"net/http"
)

//用户信息
type UserInfo struct {
	Username string `form:"username"`
	Password  string`form:"password"`
}

// 编写一个校验用户是否登录的中间件
// 其实就是从上下文中取到session data,从session data取到isLogin
func AuthMiddleware(c *gin.Context){
	// 1. 从上下文中取到session data
	// 1. 先从上下文中获取session data
	fmt.Println("in Auth")
	tmpSD, _ := c.Get(gin_session.SessionContextName)
	sd := tmpSD.(gin_session.SessionData)
	// 2. 从session data取到isLogin
	fmt.Printf("%#v\n", sd)
	value, err := sd.Get("isLogin")
	if err != nil {
		fmt.Println(err)
		// 取不到就是没有登录
		c.Redirect(http.StatusFound, "/login")
		return
	}
	fmt.Println(value)
	isLogin, ok := value.(bool)//类型断言
	if !ok {
		fmt.Println("!ok")
		c.Redirect(http.StatusFound, "/login")
		return
	}
	fmt.Println(isLogin)
	if !isLogin{
		c.Redirect(http.StatusFound, "/login")
		return
	}
	c.Next()
}

//这个是最主要的，因此涉及到表单数据的提取，cookie的设置等。
func loginHandler(c *gin.Context){
	if c.Request.Method=="POST"{//判断请求的方法，先判是否为post
		toPath := c.DefaultQuery("next", "/index")//一个路径，用于后面的重定向
		var u UserInfo
		//绑定，并解析参数
		err:=c.ShouldBind(&u)
		if err != nil {
			c.HTML(http.StatusOK, "login.html", gin.H{
				"err": "用户名或密码不能为空",
			})
			return
		}
		//解析成功
		//验证输入的账号密码受否正确
		//这里再生产中应该去数据区取信息进行比对,但这里直接写死
		if u.Username=="zhouzheng"&&u.Password=="123"{
			//接下来是核心代码
			//验证成功，,在当前sessiondata设置islogin=true
			// 登陆成功，在当前这个用户的session data 保存一个键值对：isLogin=true
			// 1. 先从上下文中获取session data
			tmpSD, ok := c.Get(gin_session.SessionContextName)
			if !ok{
				panic("session middleware")
			}
			sd := tmpSD.(gin_session.SessionData)
			// 2. 给session data设置isLogin = true
			sd.Set("isLogin", true)
			//调用Save，存储到数据库
			sd.Save()
			//跳转到index界面
			c.Redirect(http.StatusMovedPermanently,toPath)
		}else{//验证失败，重新登陆
			//返回错误和重新登陆界面
			c.HTML(http.StatusOK, "login.html", gin.H{
				"err": "用户名或密码错误",
			})
			return
		}
	}else{//get

		c.HTML(http.StatusOK, "login.html", nil)
	}
}

func indexHandler(c *gin.Context){
	c.HTML(http.StatusOK, "index.html", nil)
}

func homeHandler(c *gin.Context){
	c.HTML(http.StatusOK, "home.html", nil)
}

func vipHandler(c *gin.Context){
	c.HTML(http.StatusOK, "vip.html", nil)
}
session.go

package gin_session

import (
	"github.com/gin-gonic/gin"
)

const (
	SessionCookieName = "session_id" // sesion_id在Cookie中对应的key
	SessionContextName = "session" // session data在gin上下文中对应的key
)

//定义一个全局的Mgr
var (
	// MgrObj 全局的Session管理对象（大仓库）
	MgrObj Mgr
)

//构造一个Mgr
func InitMgr(name string,addr string,option...string){

	switch name{
	case "memory"://初始化一个内存版管理者
		MgrObj=NewMemory()
	case "redis":
		MgrObj=NewRedisMgr()
	}
	MgrObj.Init(addr,option...)//初始化mgr
}

//
type SessionData interface {
	GetID()string // 返回自己的ID
	Get(key string)(value interface{}, err error)
	Set(key string, value interface{})
	Del(key string)
	Save() // 保存
}

//不同版本的管理者接口
type Mgr interface {
	Init(addr string,option...string)
	GetSessionData(sessionId string)(sd SessionData,err error)
	CreatSession()(sd SessionData)
}

//gin框架中间件
func SessionMiddleware(mgrObj Mgr)gin.HandlerFunc{

	return func(c *gin.Context){

		//1.请求刚过来，从请求的cookie中获取SessionId
		SessionID,err:=c.Cookie(SessionCookieName)
		var sd SessionData
		if err != nil {
			//1.1 第一次来，没有sessionid，-->给用户建一个sessiondata，分配一个sessionid
			sd=mgrObj.CreatSession()
		}else {
			//1.2  取到sessionid
			//2. 根据sessionid去大仓库取sessiondata
			sd,err=mgrObj.GetSessionData(SessionID)
			if err != nil {
				//sessionid有误，取不到sessiondata，可能是自己伪造的
				//重新创建一个sessiondata
				sd=mgrObj.CreatSession()
				//更新sessionid
				SessionID=sd.GetID()//这个sessionid用于回写coookie
			}
		}
		//3. 如何实现让后续所有请求的方法都拿到sessiondata？ 让每个用户的dessiondata都不同
		//3.利用gin框架的c.Set("session",sessiondata)
		c.Set(SessionContextName,sd)
		//回写cookie
		c.SetCookie(SessionCookieName,SessionID,3600,"/","127.0.0.1",false,true)
		c.Next()
	}
}
memory.go

package gin_session

import (
	"fmt"
	uuid "github.com/satori/go.uuid"
	"sync"
)

//内存版的session服务

//SessionData支持的操作

//type MemSD struct {
//	ID string
//	Data map[string]interface{}
//	rwLock sync.RWMutex // 读写锁，锁的是上面的Data
//	// 过期时间
//}

//memory的sessiondata
type MemSD struct {
	ID string
	Data map[string]interface{}
	rwLock sync.RWMutex // 读写锁，锁的是上面的Data
	// 过期时间
}

// Get 根据key获取值
func (m *MemSD)Get(key string)(value interface{}, err error){
	// 获取读锁
	m.rwLock.RLock()
	defer m.rwLock.RUnlock()
	value, ok := m.Data[key]
	if !ok{
		err = fmt.Errorf("invalid Key")
		return
	}
	return
}

// Set 根据key获取值
func (m *MemSD)Set(key string, value interface{}){
	// 获取写锁
	m.rwLock.Lock()
	defer m.rwLock.Unlock()
	m.Data[key] = value
}

// Del 删除Key对应的键值对
func (m *MemSD)Del(key string){
	// 删除key对应的键值对
	m.rwLock.Lock()
	defer m.rwLock.Unlock()
	delete(m.Data, key)
}

//Save方法，被动设置的，因为要照顾redis版的接口
func (m *MemSD)Save(){
	return
}

//GetID 为了拿到接口的ID数据
func (m *MemSD) GetID()string{
	return m.ID

}
//管理全局的session
type MemoryMgr struct {
	Session map[string]SessionData //存储所有的session的一个大切片
	rwLock sync.RWMutex            //读写锁，用于读多写少的情况，读锁可以重复的加，写锁互斥
}

//内存版初始化session仓库
func NewMemory() (Mgr) {
	return &MemoryMgr{
		Session: make(map[string]SessionData,1024),
	}
}

//init方法
func (m *MemoryMgr)Init(addr string,option...string){
	//这里创建Init方法纯属妥协，其实memory版的并不需要初始化，前面NewMemory已经把活干完了
	//这里只是为了满足接口的定义，因为redis里需要这个方法取去连接数据库
	return
}
//GetSessionData 根据传进来的SessionID找到对应Session
func (m *MemoryMgr)GetSessionData(sessionId string)(sd SessionData,err error){
	// 获取读锁
	m.rwLock.RLock()
	defer m.rwLock.RUnlock()
	sd,ok:=m.Session[sessionId]
	if  !ok {
		err=fmt.Errorf("无效的sessionId")
		return
	}
	return
}

//CreatSession 创建一个session记录
func (m *MemoryMgr)CreatSession()(sd SessionData){
	//1. 构造一个sessionID
	uuidObj:=uuid.NewV4()
	//2.创建一个sessionData
	sd= NewMemorySessionData(uuidObj.String())
	//3.创建对应关系
	m.Session[sd.GetID()]=sd
	//返回
	return
}
//NewRedisSessionData  的构造函数,用于构造sessiondata小仓库，小红块
func NewMemorySessionData(id string)SessionData {
	return &MemSD{
		ID: id,
		Data: make(map[string]interface{},8),
	}
}
redis.go

package gin_session

import (
	"encoding/json"
	"fmt"
	uuid "github.com/satori/go.uuid"
	"strconv"
	"sync"
	"github.com/go-redis/redis"
	"time"
)

//NewRedisSessionData  的构造函数,用于构造sessiondata小仓库，小红块
func NewRedisSessionData(id string,client *redis.Client)SessionData {
	return &RedisSD{
		ID: id,
		Data: make(map[string]interface{},8),
		client:client,
	}
}

//redis版的sessiondata的数据结构
type RedisSD struct{
	ID string
	Data map[string]interface{}
	rwLock sync.RWMutex // 读写锁，锁的是上面的Data
	expired int // 过期时间
	client *redis.Client // redis连接池
}

func (r *RedisSD) Get(key string) (value interface{}, err error) {

	// 获取读锁
	r.rwLock.RLock()
	defer r.rwLock.RUnlock()
	value, ok := r.Data[key]
	if !ok{
		err = fmt.Errorf("invalid Key")
		return
	}
	return
}

func (r *RedisSD) Set(key string, value interface{}) {
	// 获取写锁
	r.rwLock.Lock()
	defer r.rwLock.Unlock()
	r.Data[key] = value
}

func (r *RedisSD) Del(key string) {
	// 删除key对应的键值对
	r.rwLock.Lock()
	defer r.rwLock.Unlock()
	delete(r.Data, key)

}

func (r *RedisSD) Save() {
	//将最新的sessiondata保存到redis中
	value,err:=json.Marshal(r.Data)
	if err != nil {
		 fmt.Printf("redis 序列化sessiondata失败 err=%v\n",err)
		return
	}
	//入库
	r.client.Set(r.ID,value,time.Duration(r.expired)*time.Second)//注意这里要用time.Duration转换一下
}

func (r *RedisSD) GetID()string{//为了拿到接口的ID数据
	return r.ID
}
//NewRedisMgr  redis版初始化session仓库,构造函数
func NewRedisMgr()(Mgr){
	//返回一个对象实例
	return &RedisMgr{
		Session: make(map[string]SessionData,1024),
	}

}

//大仓库
type RedisMgr struct{
	Session map[string]SessionData //存储所有的session的一个大切片
	rwLock sync.RWMutex
	client *redis.Client//redis连接池
}
//RedisMgr初始化
func (r *RedisMgr)Init(addr string,option...string){//这里的option...代表不定参数，参数个数不确定
	//	初始化redis连接池
	var(
		passwd string
		db string
	)
	if len(option)==1{
		passwd=option[0]
	}else if len(option)==2 {
		passwd=option[0]
		db=option[1]
	}
	//转换一下db数据类型，输入为string，需要转成int
	dbValue,err:=strconv.Atoi(db)
	if err != nil {
		dbValue=0//如果转换失败，geidb一个默认值
	}
	r.client = redis.NewClient(&redis.Options{
		Addr:     addr,
		Password: passwd, // no password set
		DB:       dbValue,  // use default DB
	})

	_, err =r.client.Ping().Result()
	if err != nil {
		panic(err)
	}
}

//加载数据库里的数据
func (r *RedisMgr)LoadFromRedis(sessionID string) (err error) {
	//1.连接redis
	//2.根据sessioniD拿到数据
	value,err:=r.client.Get(sessionID).Result()
	if err != nil {
		//redis中wusessioinid对应的sessiondata
		fmt.Errorf("连接数据库失败")
		return
	}
	//3.反序列化成 r.session
	err=json.Unmarshal([]byte(value),&r.Session)
	if err != nil {
		//反序列化失败
		fmt.Println("连接数据库失败")
		return
	}
	return
}

//GetSessionData 根据传进来的SessionID找到对应Session
func (r *RedisMgr) GetSessionData(sessionId string) (sd SessionData, err error) {

	//1.r.sesion已经从redis中拿到数据
	if r.Session==nil{
		err=r.LoadFromRedis(sessionId)
		if err != nil {
			return nil, err
		}
	}
	//2.r.session[sessionID]拿到sessionData
	// 获取读锁
	r.rwLock.RLock()
	defer r.rwLock.RUnlock()
	sd,ok:=r.Session[sessionId]
	if  !ok {
		err=fmt.Errorf("无效的sessionId")
		return
	}
	return
}

//CreatSession 创建一个session记录
func (r *RedisMgr) CreatSession() (sd SessionData) {
	//1. 构造一个sessionID
	uuidObj:=uuid.NewV4()
	//2.创建一个sessionData
	sd= NewRedisSessionData(uuidObj.String(),r.client)//从连接池中拿去一个client连接传给小红方块
	//3.创建对应关系
	r.Session[sd.GetID()]=sd
	//返回
	return
}
templates

//404.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{.username}}的home页面，登录后才能看</h1>
</body>
</html>

-----
//home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{.username}}的home页面，登录后才能看</h1>
</body>
</html>

----
//index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>index</title>
</head>
<body>
    <h1>index页面不登录也能看！</h1>
</body>
</html>

----
//login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>登录</title>
</head>
<body>
    <form action="" method="POST" enctype="application/x-www-form-urlencoded">
        <div>
            <label>用户名：
                <input type="text" name="username">
            </label>
        </div>
        <div>
            <label>密码：
                <input type="password" name="password">
            </label>
        </div>
        <div>
            <input type="submit">
        </div>
    </form>
    <p style="color: #00ffcc">{{.err}}</p>
</body>
</html>

----
//vip.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>欢迎尊敬的VIP用户：{{.username}} 光临大脚超市，奥力给！</h1>
</body>
</html>
回到顶部
预期效果
本节的目的是练习gin的基本操作和cookie与session。

通过session实现一个中间件。用来做同一的登陆校验。

如想登陆vip界面时会要求先登陆账号密码，然后才可以访问vip界面。

（1）第一次访问vip界面

mark

（2）跳转到登陆界面，输入账号密码

mark

（3）再次访问vip界面，登陆成功

mark

回到顶部
重点总结
gin框架的基本使用，包括路由，参数绑定，表单数据解析，模板渲染等。参数绑定真的很方便，它可以再绑定后解析各种形式的数据，JSON，form表单QueryString等。

gin中间件的使用，本文使用了两个中间件，一个是全局的SessionMiddleware中间件r.Use(gin_session.SessionMiddleware(gin_session.MgrObj))他用来进行session的校验和创建，首先判断用户的上下文中是否有cookie信息，SessionID,err:=c.Cookie(SessionCookieName),如果没有则创建一个用户的session仓库(用户的专属小仓库)，如果有则去该仓库中取出session数据用于之后的验证判断，这里其实还分两种情况，一种就是用户cookie里的sessionid过期了，所以要重新创建；另外一中就是成功取到了sessiondata。取到sessiondata后就涉及到一个问题，即使如何将sessiondata传递给后面的鉴权中间件AuthMiddleware（用户判断用户是否登陆：sessiondata中islogin字段是否等于true），这里采用的c.Set(SessionContextName,sd),这是在上下文context中存储一个key-value，再之后的AuthMiddleware中间件中可以使用c.Get(gin_session.SessionContextName)取出sessiondata完成传递。

在session的结构上可以划分为两部分：一个是整体的session大仓库，里面存储该网站所有的用户的sessiondata，他使用一个大map来维护，他使用数据结构Mgr来进行管理；这里面的sessiondata又是一个小仓库，里面存储每个用户的具体session信息，他使用数据结构SessionData来维护。

由于session中间件要实现不同的版本，因此这里涉及到面向接口的编程。如本例中大仓库和先仓库均要实现memory版本和redis版本，因此他们都要设计成接口的形式。大仓库Mgr接口要实现的方法有

type Mgr interface {
	Init(addr string,option...string)
	GetSessionData(sessionId string)(sd SessionData,err error)
	CreatSession()(sd SessionData)
}
小仓库sessiondata要实现的方法有

type SessionData interface {
   GetID()string // 返回自己的ID
   Get(key string)(value interface{}, err error)
   Set(key string, value interface{})
   Del(key string)
   Save() // 保存
}
大仓库和小仓库在使用之前都需要初始化，那么他们各自在哪里初始化呢？大仓库在在运行开始就需要初始化，根据传入的参数时“memory”还是“redis”决定初始化什么版本的大仓库（用构造函数，返回一个对象实例），之后又调用了一个初始化函数MgrObj.Init(addr,option...)//初始化mgr，这个初始化和函数其实是为redis单独创建的，目的是初始化redis连接池，这里其实也可以把他们放进构造函数NewRedisMgr中；小仓库sessiondata实在session中间件中用sd=mgrObj.CreatSession()创建的。注意这里初始化了里面维护的map，大仓库真正写入数据是在创建了sessiondata后，小仓库写入数据是在登陆成功后的设置的islogin=true。

关于操作redis，本文使用的第三方库是github.com/go-redis/redis还可以使用github.com/garyburd/redigo/redis

在创建用户的小仓库sessiondata时，需要给每个用户分配一个独有的sessionid，这里使用了第三方库github.com/satori/go.uuid,单有一些问题，就是他的uuid是字符串型的，不太方便检索，因此可以使用snowflake算法来生成一个全局的全局ID，具体使用方法请自行百度。

整理一下代码的流程

程序首先根据传入信息，选择中间件版本memory还是redis，然后取初始化他们的管理者实例（大仓库），在选择redis时还要初始化一下连接池。

用户访问服务器的/vip界面

首先进入全局的中间件SessionMiddleware，目的是为了拿出用户cookie里对应的小仓库数据，如果用户第一次来，那就给他创建一个专属的小仓库。该中间件结束时，会在用户的context中设置一个key-value，存储着用户的小仓库session数据。并且用户拿到了一个全新的cookie（就像是一把钥匙）。

接下来金进入鉴权中间件。他的作用是检查上下文context中用户的小仓库内容（sessiondata），里面是否有islogin=true的字段，如果没有，在就重定向到login界面是实现登录。

在login姐买你输入账号密码并验证成功后，会在用户小仓库sessiondata中写入islogin=true的字段

再次访问/vip，会再次走一遍两个中间件，并且完成验证，最终到达vipHandler，给用户返回vip登陆成功界面。
https://www.cnblogs.com/wind-zhou/p/13114548.html