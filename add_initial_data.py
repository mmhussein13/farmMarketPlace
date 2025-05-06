import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_ecommerce.settings')
django.setup()

from store.models import Category, Product
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
import random
import base64

def create_categories():
    """Create the required categories for the mixed farming business"""
    categories = [
        {
            'name': 'Chicken',
            'description': 'Fresh farm-raised chicken products'
        },
        {
            'name': 'Ducks',
            'description': 'Free-range duck products directly from our farm'
        },
        {
            'name': 'Fish',
            'description': 'Fresh-water fish raised in our sustainable ponds'
        },
        {
            'name': 'Sheep',
            'description': 'Organic sheep products from our farm'
        },
        {
            'name': 'Goats',
            'description': 'Free-range goat products from our sustainable farm'
        },
        {
            'name': 'Cow',
            'description': 'Grass-fed beef and dairy products'
        },
        {
            'name': 'Vegetables',
            'description': 'Fresh organic vegetables grown on our farm'
        },
        {
            'name': 'Fruits',
            'description': 'Seasonal fruits grown without pesticides'
        },
        {
            'name': 'Honey',
            'description': 'Pure, raw honey produced from our own beehives'
        }
    ]
    
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'description': category_data['description']
            }
        )
        
        # Generate a simple SVG placeholder for the category
        svg_content = f'''
        <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="200" height="200" fill="{random_color()}" />
            <text x="100" y="100" font-family="Arial" font-size="20" text-anchor="middle" fill="white">{category.name}</text>
        </svg>
        '''
        
        if created or not category.image:
            category.image.save(
                f"{category.slug}.svg", 
                ContentFile(svg_content.encode()),
                save=True
            )
            
        print(f"{'Created' if created else 'Updated'} category: {category.name}")
    
    return Category.objects.all()

def random_color():
    """Generate a random color for SVG backgrounds"""
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#34495e', '#d35400', '#c0392b']
    return random.choice(colors)

def create_products(categories):
    """Create sample products for each category"""
    products = []
    
    # Chicken products
    chicken = categories.get(name='Chicken')
    products.extend([
        {'name': 'Whole Chicken', 'category': chicken, 'price': 12.99, 'stock': 50, 
         'description': 'Farm-raised whole chicken, ready to cook.'},
        {'name': 'Chicken Breast', 'category': chicken, 'price': 8.99, 'stock': 100, 
         'description': 'Boneless chicken breast, perfect for grilling or baking.'},
        {'name': 'Chicken Eggs (Dozen)', 'category': chicken, 'price': 4.99, 'stock': 200, 
         'description': 'Fresh farm eggs from free-range chickens.'}
    ])
    
    # Duck products
    duck = categories.get(name='Ducks')
    products.extend([
        {'name': 'Whole Duck', 'category': duck, 'price': 18.99, 'stock': 30, 
         'description': 'Fresh farm-raised duck, perfect for roasting.'},
        {'name': 'Duck Eggs (Half Dozen)', 'category': duck, 'price': 5.99, 'stock': 50, 
         'description': 'Rich and flavorful duck eggs from our farm.'}
    ])
    
    # Fish products
    fish = categories.get(name='Fish')
    products.extend([
        {'name': 'Fresh Tilapia', 'category': fish, 'price': 9.99, 'stock': 40, 
         'description': 'Farm-raised tilapia, cleaned and ready to cook.'},
        {'name': 'Catfish Fillet', 'category': fish, 'price': 11.99, 'stock': 35, 
         'description': 'Fresh catfish fillets from our sustainable ponds.'}
    ])
    
    # Sheep products
    sheep = categories.get(name='Sheep')
    products.extend([
        {'name': 'Lamb Chops', 'category': sheep, 'price': 15.99, 'stock': 30, 
         'description': 'Tender lamb chops from our organic farm.'},
        {'name': 'Ground Lamb', 'category': sheep, 'price': 10.99, 'stock': 45, 
         'description': 'Lean ground lamb perfect for meatballs or burgers.'}
    ])
    
    # Goat products
    goat = categories.get(name='Goats')
    products.extend([
        {'name': 'Goat Meat', 'category': goat, 'price': 14.99, 'stock': 25, 
         'description': 'Fresh goat meat from our farm, perfect for stews and curries.'},
        {'name': 'Goat Milk (1L)', 'category': goat, 'price': 6.99, 'stock': 40, 
         'description': 'Fresh, raw goat milk, bottled daily.'}
    ])
    
    # Cow products
    cow = categories.get(name='Cow')
    products.extend([
        {'name': 'Ground Beef', 'category': cow, 'price': 9.99, 'stock': 60, 
         'description': 'Grass-fed ground beef, lean and flavorful.'},
        {'name': 'Ribeye Steak', 'category': cow, 'price': 19.99, 'stock': 25, 
         'description': 'Premium cut ribeye steak from our grass-fed cows.'},
        {'name': 'Fresh Milk (1L)', 'category': cow, 'price': 3.99, 'stock': 100, 
         'description': 'Farm-fresh cow milk, pasteurized and ready to drink.'}
    ])
    
    # Vegetable products
    vegetables = categories.get(name='Vegetables')
    products.extend([
        {'name': 'Organic Tomatoes', 'category': vegetables, 'price': 2.99, 'stock': 150, 
         'description': 'Vine-ripened tomatoes grown without pesticides.'},
        {'name': 'Leafy Greens Mix', 'category': vegetables, 'price': 3.99, 'stock': 100, 
         'description': 'A mix of kale, spinach, and other seasonal greens.'},
        {'name': 'Fresh Carrots (Bundle)', 'category': vegetables, 'price': 2.49, 'stock': 120, 
         'description': 'Organic carrots, freshly harvested.'}
    ])
    
    # Fruit products
    fruits = categories.get(name='Fruits')
    products.extend([
        {'name': 'Seasonal Berry Mix', 'category': fruits, 'price': 6.99, 'stock': 80, 
         'description': 'A mix of strawberries, blueberries, and raspberries in season.'},
        {'name': 'Organic Apples (4-pack)', 'category': fruits, 'price': 4.99, 'stock': 90, 
         'description': 'Crisp, sweet apples grown on our farm.'}
    ])
    
    # Honey products
    honey = categories.get(name='Honey')
    products.extend([
        {'name': 'Raw Honey (16oz)', 'category': honey, 'price': 8.99, 'stock': 70, 
         'description': 'Pure, unfiltered honey from our own beehives.'},
        {'name': 'Honeycomb', 'category': honey, 'price': 12.99, 'stock': 30, 
         'description': 'Natural honeycomb, straight from the hive.'}
    ])
    
    for product_data in products:
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'category': product_data['category'],
                'description': product_data['description'],
                'price': product_data['price'],
                'stock': product_data['stock'],
                'is_available': True
            }
        )
        
        # Generate a simple SVG placeholder for the product
        svg_content = f'''
        <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="300" height="300" fill="{random_color()}" />
            <text x="150" y="150" font-family="Arial" font-size="20" text-anchor="middle" fill="white">{product.name}</text>
            <text x="150" y="180" font-family="Arial" font-size="16" text-anchor="middle" fill="white">${product.price}</text>
        </svg>
        '''
        
        if created or not product.image:
            product.image.save(
                f"{product.slug}.svg", 
                ContentFile(svg_content.encode()),
                save=True
            )
            
        print(f"{'Created' if created else 'Updated'} product: {product.name}")

if __name__ == '__main__':
    print("Creating initial categories and products...")
    categories = create_categories()
    create_products(categories)
    print("Done!")