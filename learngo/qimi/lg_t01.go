package main  // 声明 main 包，表明当前是一个可执行程序

import "fmt"  // 导入内置 fmt 包

func main(){  // main函数，是程序执行的入口
	fmt.Println("Hello World!")  // 在终端打印 Hello World!
}
mod包缺少模块：--》  go mod tidy
// goland： project项目创建代理设置= proxy： https://goproxy.cn
// 直接运行go文件		==》  go run hello.go
// 在hello.go目录下执行  ==》 go build
// 不在go文件目录下执行	  ==》 go build hello
// -o编译指定可执行的文件名字 ==》 go build -o heihei.exe

// 类型	描述
// uint8	无符号 8位整型 (0 到 255)
// uint16	无符号 16位整型 (0 到 65535)
// uint32	无符号 32位整型 (0 到 4294967295)
// uint64	无符号 64位整型 (0 到 18446744073709551615)
// int8	有符号 8位整型 (-128 到 127)
// int16	有符号 16位整型 (-32768 到 32767)
// int32	有符号 32位整型 (-2147483648 到 2147483647)
// int64	有符号 64位整型 (-9223372036854775808 到 9223372036854775807)
// uint	32位操作系统上就是uint32，64位操作系统上就是uint64
// int	32位操作系统上就是int32，64位操作系统上就是int64
// uintptr	无符号整型，用于存放一个指针

//文件–>首选项—>设置—>用户设置 => useCodeSnippetsOnFunctionSuggest打勾 ;;补全代码
