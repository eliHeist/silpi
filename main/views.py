from django.shortcuts import render, resolve_url
from django.views import View
from django.views.generic import TemplateView
from django.templatetags.static import static
from posts.models import Post

from products.models import Category

# Create your views here.

class IndexView(View):
    def get(self, request):
        template_name = "main/index.html"
        posts = Post.objects.all().order_by('date_modified')[:3]

        carousel_slides = [
            {
                "title": """Discover a world <br/>of <span class="text-primary">vehicles!</span>""",
                "image_url": static('images/vehicles.webp'),
                "description": """
                    Whether you're looking to buy your dream car or simply need a reliable vehicle for rent, you've come to the right place. Buy or rent your perfect ride with us.
                """,
                "url": resolve_url('vehicles:list'),
            },
            {
                "title": """Expert <span class="text-primary">Consultancy</span> <br/>Services""",
                "image_url": static('images/cunsultancy.webp'),
                "description": "Unlock greater potential in your business with our expert consultancy services.",
                "url": resolve_url('consultancy:consultancy'),
            },
            {
                "title": """Farm <span class="text-primary">Fresh</span> Goodness""",
                "image_url": static('images/farm-tractor.webp'),
                "description": "Explore a bountiful harvest of fruits, adorable animals, and animal products straight from the farm to your table.",
                "url": resolve_url('products:categories'),
            },
        ]

        services = [
            {
                "title": "Consultancy",
                "description": "Our consultancy services are designed to provide expert guidance and solutions to individuals and businesses. Whether you need strategic advice, process optimization, or specialized expertise, we have a team of experienced consultants ready to assist you.",
                "image": static('images/consultancy.webp'),
                "links": [
                    {
                        "text": "Find out more",
                        "url": resolve_url('consultancy:consultancy')
                    }
                ]
            },
            {
                "title": "Micro Lending",
                "description": "We offer micro-lending services tailored to small businesses and entrepreneurs. Whether you're looking to start or expand your business, our micro-loans provide the financial support you need without the complexities of traditional loans.",
                "image": static('images/loaning.webp'),
                "links": [
                    {
                        "text": "Find out more",
                        "url": resolve_url('main:micro-loans')
                    }
                ]
            },
            {
                "title": "Farming and Agriculture",
                "description": "Our farming services encompass the cultivation and sale of a wide range of agricultural products, including fruits, vegetables, livestock, and animal meat. We are committed to sustainable farming practices and delivering high-quality products to our customers.",
                "image": static('images/farming.webp'),
                "links": [
                    {
                        "text": "Find out more",
                        "url": resolve_url('products:categories')
                    }
                ]
            },
            {
                "title": "Vehicles for Sale and Hire",
                "description": "We offer a diverse range of vehicles for both sale and hire. Whether you're looking to purchase a reliable vehicle or need a rental for a specific purpose, our fleet includes a variety of options to meet your transportation needs.",
                "image": static('images/vehicle-hire.webp'),
                "links": [
                    {
                        "text": "Find out more",
                        "url": resolve_url('vehicles:list')
                    }
                ]
            }
        ]

        context = {
            'categories': Category.objects.all(),
            'posts': posts,
            'carousel_slides': carousel_slides,
            'services': services
        }
        return render(request, template_name, context)

class AboutView(View):
    def get(self, request):
        template_name = "main/about.html"
        context = {}
        return render(request, template_name, context)  

class TermsAndPrivacyView(View):
    def get(self, request):
        template_name = "main/terms-privacy.html"
        context = {}
        return render(request, template_name, context) 


class MicroLoanView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'main/microloans.html'
        context = {}
        return render(request, template_name, context) 


class PaintView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'main/paints.html'
        products = [
            {
                "name": "Vinyl Silk",
                "description": "For a luxurious, smooth finish.",
                "bg_class": "bg-primary text-light"
            },
            {
                "name": "Vinyl Matt",
                "description": "Ideal for a modern, flat look.",
                "bg_class": "bg-secondary text-light"
            },
            {
                "name": "Weather Guard",
                "description": "Perfect for exterior protection.",
                "bg_class": "bg-dark text-light"
            },
            {
                "name": "Budget Emulsion",
                "description": "Affordable quality for everyday use.",
                "bg_class": "bg-white text-dark"
            }
        ]

        colors = [
            {
                "name": "Broken White",
                "hex": "#F8F8F2",
                "mood": "Gives a clean, airy, and spacious feel to the space.",
                "foreground_color": "#CFCFCF"  # Light grey shade for contrast
            },
            {
                "name": "Off White",
                "hex": "#F5F5DC",
                "mood": "Creates a warm and inviting atmosphere.",
                "foreground_color": "#BBBBAA"  # Light grey-brown shade for contrast
            },
            {
                "name": "Butter",
                "hex": "#F3E5AB",
                "mood": "Brings a cheerful and cozy feel to the room.",
                "foreground_color": "#B8AA77"  # Shade of butter color for contrast
            },
            {
                "name": "Vanilla",
                "hex": "#F3E5AB",
                "mood": "Adds a soft and comforting vibe.",
                "foreground_color": "#B8AA77"  # Shade of vanilla color for contrast
            },
            {
                "name": "Ivory",
                "hex": "#FFFFF0",
                "mood": "Provides a classic and timeless look.",
                "foreground_color": "#CCCCCC"  # Light grey shade for contrast
            },
            {
                "name": "Sunlight Yellow",
                "hex": "#FFFD37",
                "mood": "Energizes and brightens up the space.",
                "foreground_color": "#B8B700"  # Shade of yellow for contrast
            },
            {
                "name": "Mint Green",
                "hex": "#98FF98",
                "mood": "Creates a refreshing and calming ambiance.",
                "foreground_color": "#6ACF6A"  # Shade of mint green for contrast
            },
            {
                "name": "Apple Green",
                "hex": "#8DB600",
                "mood": "Gives a lively and invigorating feeling.",
                "foreground_color": "#5C7800"  # Shade of apple green for contrast
            },
            {
                "name": "Milo Green",
                "hex": "#4CBB17",
                "mood": "Adds a vibrant and energetic touch.",
                "foreground_color": "#35680F"  # Shade of milo green for contrast
            },
            {
                "name": "Mermaid Green",
                "hex": "#30BA8F",
                "mood": "Brings a soothing and serene vibe.",
                "foreground_color": "#25705B"  # Shade of mermaid green for contrast
            },
            {
                "name": "Soft Blue",
                "hex": "#ADD8E6",
                "mood": "Creates a peaceful and tranquil atmosphere.",
                "foreground_color": "#85AFC5"  # Shade of soft blue for contrast
            },
            {
                "name": "Blue",
                "hex": "#0000FF",
                "mood": "Adds a bold and confident touch.",
                "foreground_color": "#0000B3"  # Shade of blue for contrast
            },
            {
                "name": "Deep Blue",
                "hex": "#00008B",
                "mood": "Gives a sophisticated and calming feel.",
                "foreground_color": "#000066"  # Dark shade of blue for contrast
            },
            {
                "name": "Light Purple",
                "hex": "#D8BFD8",
                "mood": "Adds a soft and romantic touch.",
                "foreground_color": "#B494B4"  # Shade of light purple for contrast
            },
            {
                "name": "Deep Purple",
                "hex": "#800080",
                "mood": "Gives a rich and luxurious feel.",
                "foreground_color": "#590059"  # Dark shade of purple for contrast
            },
            {
                "name": "Pink",
                "hex": "#FFC0CB",
                "mood": "Brings a playful and charming atmosphere.",
                "foreground_color": "#B38D92"  # Shade of pink for contrast
            },
            {
                "name": "Terracotta",
                "hex": "#E2725B",
                "mood": "Creates a warm and earthy vibe.",
                "foreground_color": "#A33F2F"  # Shade of terracotta for contrast
            },
            {
                "name": "Magnolia",
                "hex": "#F8F4FF",
                "mood": "Adds a delicate and elegant touch.",
                "foreground_color": "#B8B4CC"  # Light grey-purple shade for contrast
            },
            {
                "name": "Cream",
                "hex": "#FFFDD0",
                "mood": "Provides a light and soothing atmosphere.",
                "foreground_color": "#CCC99F"  # Light grey-beige shade for contrast
            },
            {
                "name": "Student Cream",
                "hex": "#FFFDD0",
                "mood": "Creates a bright and focused environment.",
                "foreground_color": "#CCC99F"  # Light grey-beige shade for contrast
            },
            {
                "name": "Peach",
                "hex": "#FFE5B4",
                "mood": "Brings a warm and friendly feel to the space.",
                "foreground_color": "#B3997A"  # Shade of peach for contrast
            },
            {
                "name": "Mango",
                "hex": "#FF8243",
                "mood": "Adds a vibrant and energetic vibe.",
                "foreground_color": "#B35929"  # Shade of mango for contrast
            },
            {
                "name": "Beige",
                "hex": "#F5F5DC",
                "mood": "Creates a neutral and calm atmosphere.",
                "foreground_color": "#B5B59A"  # Shade of beige for contrast
            },
            {
                "name": "Light Stone",
                "hex": "#D3D3D3",
                "mood": "Gives a modern and sleek look.",
                "foreground_color": "#A6A6A6"  # Shade of grey for contrast
            },
            {
                "name": "Deep Stone",
                "hex": "#8B4513",
                "mood": "Adds a strong and rustic feel.",
                "foreground_color": "#65330E"  # Dark shade of brown for contrast
            },
            {
                "name": "Smoke Grey",
                "hex": "#708090",
                "mood": "Creates a cool and contemporary atmosphere.",
                "foreground_color": "#4D5963"  # Shade of grey for contrast
            },
            {
                "name": "Grey",
                "hex": "#808080",
                "mood": "Provides a balanced and neutral feel.",
                "foreground_color": "#595959"  # Shade of grey for contrast
            },
            {
                "name": "Charcoal Black",
                "hex": "#36454F",
                "mood": "Gives a bold and dramatic touch.",
                "foreground_color": "#1D2A33"  # Dark shade of charcoal for contrast
            }
        ]

        context = {
            'products': products,
            'colors': colors
        }
        return render(request, template_name, context) 

