"""Sale Model and Data storage functions"""


class Sales():
    """This class defines the Sales Model and
        the various methods of manipulating the Sales data"""

    sale_id = 1
    salesRecords = []

    def __init__(self, names, cart, price):
        """Initialize the Sales Model with constructor"""

        self.sale_id = len(Sales.salesRecords) + 1
        self.cart = cart
        self.names = names
        self.price = price
        

    def post_sales(self):
        """Sale method to make a sale record"""

        items = dict(
            sale_id=self.sale_id,
            cart=self.cart,
            names=self.names,
            price=self.price
        
        )
        Sales.salesRecords.append(items)
        return items

    def get_all_sales(self):
        """Sale method to fetch all sales"""
        return Sales.salesRecords

    @staticmethod
    def get_one_sale(sale_id):
        """Sale method to fetch a single sale record"""
        sale_record = [sale for sale in Sales.salesRecords if sale['sale_id'] == sale_id]
        if sale_record:
            return sale_record
        return 'not found'