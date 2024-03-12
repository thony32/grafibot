import ampalibe
from ampalibe import Messenger, Model, Payload
# from ampalibe import translate
from ampalibe.ui import QuickReply, Element, Button, Type
from ampalibe.messenger import Action, Filetype
from conf import Configuration

bot = ampalibe.init(Configuration())
chat = Messenger()
query = Model()

# create a get started option to get permission of user.
chat.get_started()


# NOTE: Starting discussion
@ampalibe.command('/')
def main(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen) # mark the message as seen
    chat.send_action(sender_id, Action.typing_on) # turn on the typing indicator
    chat.send_action(sender_id, Action.typing_off) # turn off the typing indicator
    chat.send_text(sender_id, "Bienvenue sur Grafikaly, votre source en ligne pour des produits numériques créatifs!")
    quick_replies = [QuickReply(title = "Catalogue", payload=Payload("/catalog")), QuickReply(title = "Promotion", payload=Payload("/about")), QuickReply(title = "Assistance", payload=Payload("/assistance"))]
    chat.send_quick_reply(sender_id, quick_replies, "Comment puis-je vous aider aujourd'hui?")
    # query.set_action(sender_id, '/get_name') # set the action to get the name of the user
    

# NOTE: Catalog Section    
@ampalibe.command('/catalog')
def catalog(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    quick_replies = [QuickReply(title = "Abonnement", payload=Payload("/subscription")), QuickReply(title = "Outils Numériques", payload=Payload("/numeric_tools")), QuickReply(title = "Streaming", payload=Payload("/streaming")), QuickReply(title = "Jeux Vidéos", payload=Payload("/games"))]
    chat.send_quick_reply(sender_id, quick_replies, "Veuillez choisir une catégorie de produit")
    # query.set_action(sender_id, None) # destroy and remove the action

########## NOTE: Subscription Section
@ampalibe.command('/subscription')
def catalog_subscription(sender_id, cmd, **ext):
    
    buttons = []
    list_items = []
    
    buttons = [
        Button(
            type=Type.postback,
            title="Voir Produit",
            payload=Payload("https://www.grafikaly.mg/shop/prime-video-06-mois-promo-nouvel-an-2024-495?category=22", id_item=2),
        )
    ]
    
    list_items = [
        Element(
            title="Prime Video 6 Mois - Promo 2024",
            image_url="https://www.grafikaly.mg/web/image/product.template/495/image_512/PRIME%20VIDEO%20%2806%20Mois%29%20-%20PROMO%20NOUVEL%20AN%202024?unique=3d85dba",
            buttons=buttons,
        ),
        Element(
            title="Prime Video 6 Mois - Promo 2024",
            image_url="https://www.grafikaly.mg/web/image/product.template/495/image_512/PRIME%20VIDEO%20%2806%20Mois%29%20-%20PROMO%20NOUVEL%20AN%202024?unique=3d85dba",
            buttons=buttons,
        ),
        Element(
            title="Prime Video 6 Mois - Promo 2024",
            image_url="https://www.grafikaly.mg/web/image/product.template/495/image_512/PRIME%20VIDEO%20%2806%20Mois%29%20-%20PROMO%20NOUVEL%20AN%202024?unique=3d85dba",
            buttons=buttons,
        )]
    
    chat.send_text(sender_id, "Voici les abonnements disponibles")
    chat.send_generic_template(sender_id, list_items, next=True)

# SECTION Outils Numériques
@ampalibe.command('/numeric_tools')
def numeric_tools(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    # Ici, ajoutez votre code pour lister les outils numériques
    # ...

# SECTION Streaming
@ampalibe.command('/streaming')
def streaming(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    # Ici, ajoutez votre code pour lister les options de streaming
    # ...

# SECTION Jeux Vidéos
@ampalibe.command('/games')
def games(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    # Ici, ajoutez votre code pour lister les jeux vidéos
    # ...

# SECTION Promotion
@ampalibe.command('/promotion')
def promotion(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    # Ici, ajoutez votre code pour afficher les promotions
    chat.send_text(sender_id, "Voici nos meilleures offres en promotions:")
    # ...

# SECTION Assistance
@ampalibe.command('/assistance')
def assistance(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    quick_replies = [
        QuickReply(title="Réclamation", payload=Payload("/claim")),
        QuickReply(title="Suivi de commande", payload=Payload("/order_followup")),
        QuickReply(title="Demande spécifique", payload=Payload("/specific_request"))
    ]
    chat.send_quick_reply(sender_id, quick_replies, "Comment puis-je vous assister?")
    # ...

# SECTION Réclamation
@ampalibe.command('/claim')
def claim(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    chat.send_text(sender_id, "Donnez le plus de détails possible à propos de votre réclamation.")
    # Définissez ici l'action pour capturer les détails de la réclamation de l'utilisateur
    # ...

# SECTION Suivi de commande
@ampalibe.command('/order_followup')
def order_followup(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    chat.send_text(sender_id, "Veuillez saisir la référence de votre commande/facture.")
    # Définissez ici l'action pour capturer la référence de commande de l'utilisateur
    # ...

# SECTION Demande spécifique
@ampalibe.command('/specific_request')
def specific_request(sender_id, cmd, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    chat.send_action(sender_id, Action.typing_off)
    chat.send_text(sender_id, "Posez-nous votre question, notre équipe vous répondra dès que possible.")
    # Définissez ici l'action pour capturer la question spécifique de l'utilisateur
    # ...
