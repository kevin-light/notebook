css选择器选择第n个子元素，共有两种写法：

.parent span:nth-child(n) 选择parent下的第n个子元素（不管前边是不是span，都算在内）

.parent span:nth-of-type(n) 选择parent下的第n个span元素（强调只对span标签计数）

.parent span.one:nth-of-type(n) 并不会选中第n个带有.one 的 class的span元素