from selenium.webdriver.common.by import By
"""以下为项目服务器地址"""
URL = "http://localhost:3306"

"""以下为登录模块配涉及元素 配置信息"""
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
login_username = By.CSS_SELECTOR, "#username"
login_pwd = By.CSS_SELECTOR, "#password"
login_verify_code = By.CSS_SELECTOR, "#verify_code"
login_btn = By.CSS_SELECTOR, ".J-login-submit"
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
login_err_ok_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
login_logout_link = By.PARTIAL_LINK_TEXT, "安全退出"

"""以下数据为购物车配置数据"""
cart_link = By.PARTIAL_LINK_TEXT, "首页"
# 搜索框
cart_search = By.CSS_SELECTOR, "#q"
# 搜索按钮
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 添加购物车--》跳转至详情页
cart_add_info = By.CSS_SELECTOR, ".p-btn>a"
# 添加购物车
cart_add = By.CSS_SELECTOR, "#join_cart"
# iframe表单名称
cart_frame_id = By.CSS_SELECTOR, "#layui-layer-iframe1"
# 获取添加购物车结果
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
# 关闭提示窗口
cart_close_window = By.CSS_SELECTOR, ".layui-layer-close"
"""以下为订单页面的配置数据"""
order_link = By.PARTIAL_LINK_TEXT, "首页"
# 我的购物车
order_my_cart = By.CSS_SELECTOR, ".c-n"
# 去结算
order_account = By.CSS_SELECTOR, ".gwc-qjs"
# 全选
order_all = By.CSS_SELECTOR, ".checkCartAll"
# 收货人 备用
order_person = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_submit = By.CSS_SELECTOR, ".Sub-orders"
# 获取提交订单结果
order_submit_result= By.CSS_SELECTOR, ".erhuh>h3"
"""以下为支付模块配置数据"""
# 我的订单
pay_my_order = By.PARTIAL_LINK_TEXT, "我的订单"
# 我的订单 页面title 注意：此处为变量，不需要By
pay_my_order_title = "我的订单"
# 立即支付
pay_now_payment = By.CSS_SELECTOR, ".ps_lj"
# 支付页面title
pay_payment_title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
# 货到付款
pay_on_delivery = By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"
# 确认支付
pay_confirm_payment = By.CSS_SELECTOR, ".button-confirm-payment"
# 获取支付结果
pay_payment_result = By.CSS_SELECTOR, ".erhuh>h3"


