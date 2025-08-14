class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if 'session_key' not in request.session:
            cart = self.session['cart'] = {}

        self.cart = cart