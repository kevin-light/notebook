
`使用 Ant Design for Vue 的 Menu 组件，引入并注册了，发现点击的时候，下拉菜单样式无法正常显示，控制台报错 TypeError: Cannot read property 'propsData' of undefined 。
引入 Menu 组件：
import { Menu } from 'ant-design-vue';
注册 Menu 组件：因为下拉菜单是 <a-menu-item> 所以还要注册一下 Menu.Item 。
Vue.component(Menu.name, Menu);
Vue.component(Menu.Item.name, Menu.Item);
也可以使用 Vue.use(Menu); 全局注册。
下面两种报错，也可以用此方法解决，原理是类似的`