class Product():

    product_id = 1
    productRecord = []


    def __init__(self, product_name, category, description, inventory, price):

        self.product_id = len(Product.productRecord) + 1
        self.product_name = product_name
        self.category = category
        self.description = description
        self.inventory = inventory
        self.price = price

    def post_product(self):
        

        items = dict(

            product_id=self.product_id,
            product_name=self.product_name,
            category=self.category,
            description=self.description,
            inventory=self.inventory,
            price=self.price,
            
        )
        Product.productRecord.append(items)
        return items

    def get_all_products(self):

        return Product.productRecord

    @staticmethod
    def get_one_product(product_id):

       
        one_item = [product for product in Product.productRecord if product['product_id'] == product_id]
        if one_item:
            return one_item
        return 'product not available'

   
    
        