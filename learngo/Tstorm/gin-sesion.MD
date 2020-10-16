在Gin框架中，我们可以依赖gin-contrib/sessions中间件处理session。

gin-contrib/sessions中间件支持的存储引擎：
cookie
memstore
redis
memcached
mongodb
下面介绍session的用法

1.安装session包
go get github.com/gin-contrib/sessions
2.基本的session用法
package main

import (
        // 导入session包
	"github.com/gin-contrib/sessions"
       // 导入session存储引擎
	"github.com/gin-contrib/sessions/cookie"
        // 导入gin框架包
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
        // 创建基于cookie的存储引擎，secret11111 参数是用于加密的密钥
	store := cookie.NewStore([]byte("secret11111"))
        // 设置session中间件，参数mysession，指的是session的名字，也是cookie的名字
       // store是前面创建的存储引擎，我们可以替换成其他存储引擎
	r.Use(sessions.Sessions("mysession", store))

	r.GET("/hello", func(c *gin.Context) {
                // 初始化session对象
		session := sessions.Default(c)
                
                // 通过session.Get读取session值
                // session是键值对格式数据，因此需要通过key查询数据
		if session.Get("hello") != "world" {
                        // 设置session数据
			session.Set("hello", "world")
                        // 删除session数据
                        session.Delete("tizi365")
                        // 保存session数据
			session.Save()
                        // 删除整个session
                        // session.Clear()
		}
                
		c.JSON(200, gin.H{"hello": session.Get("hello")})
	})
	r.Run(":8000")
}
2.基于redis存储引擎的session
如果我们想将session数据保存到redis中，只要将session的存储引擎改成redis即可。

使用redis作为存储引擎的例子：

首先安装redis存储引擎的包

go get github.com/gin-contrib/sessions/redis
例子：

package main

import (
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/redis"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	// 初始化基于redis的存储引擎
	// 参数说明：
	//    第1个参数 - redis最大的空闲连接数
	//    第2个参数 - 数通信协议tcp或者udp
	//    第3个参数 - redis地址, 格式，host:port
	//    第4个参数 - redis密码
	//    第5个参数 - session加密密钥
	store, _ := redis.NewStore(10, "tcp", "localhost:6379", "", []byte("secret"))
	r.Use(sessions.Sessions("mysession", store))

	r.GET("/incr", func(c *gin.Context) {
		session := sessions.Default(c)
		var count int
		v := session.Get("count")
		if v == nil {
			count = 0
		} else {
			count = v.(int)
			count++
		}
		session.Set("count", count)
		session.Save()
		c.JSON(200, gin.H{"count": count})
	})
	r.Run(":8000")
}