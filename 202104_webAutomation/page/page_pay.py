import page
from base.base import Base
from time import sleep


class PagePay(Base):
    def page_click_index(self):
        self.base_click(page.order_link)

    # 点击 我的订单链接
    def page_click_my_order_link(self):
        self.base_click(page.pay_my_order)

    # 点击 立即支付
    def page_click_now_payment(self):
        # 必须先切换窗口
        self.base_switch_to_window(page.pay_my_order_title)
        # 点击立即支付
        self.base_click(page.pay_now_payment)

    # 点击 货到付款
    def page_click_pay_on_delivery(self):
        # 必须切换窗口
        self.base_switch_to_window(page.pay_payment_title)
        # 点击货到付款
        self.base_click(page.pay_on_delivery)

    # 确认支付方式
    def page_click_payment_mode(self):
        self.base_click(page.pay_confirm_payment)

    # 获取支付结果
    def page_get_payment_result(self):
        return self.base_get_text(page.pay_payment_result)

    # 组合业务方法
    def page_pay(self):
        self.page_click_my_order_link()
        self.page_click_now_payment()
        self.page_click_pay_on_delivery()
        self.page_click_payment_mode()