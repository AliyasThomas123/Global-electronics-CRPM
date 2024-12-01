from repository.purchase_repository import PurchaseRepository
class AnalyticsService:
    @staticmethod
    def generate_report(report_type):
        if report_type == "sales":
            return PurchaseRepository.get_sales_summary()
        elif report_type == "top_customers":
            return PurchaseRepository.get_top_customers()
        elif report_type == "product_performance":
            return PurchaseRepository.get_product_performance()
        else:
            raise ValueError("Invalid report type.")
