# -*- coding: utf-8 -*-
"""Génère le site multi-pages de la Miroiterie Winter (HTML statique + style.css).
Usage : python3 generer_site.py <dossier_du_depot>
"""
import json, os, sys, html
from departements import DEPARTEMENTS, DEP_EXISTANTES, THEMES, NOUVELLES_VILLES

OUT = sys.argv[1]
DOMAINE = "https://miroiterie-winter.fr"
TEL = "07 83 38 68 24"
TEL_LIEN = "tel:+33783386824"
MAIL = "miroiterie.winter@gmail.com"
ADRESSE = "141 rue du Général Leclerc, 93110 Rosny-sous-Bois"
NOTE, NB_AVIS = "4,9", 60
INSTAGRAM = "https://www.instagram.com/miroiterie_winter/"
MAPS = "https://maps.google.com/maps?cid=10857902701694603854"
AVIS = "https://search.google.com/local/writereview?placeid=ChIJ51-lGxwT5kcRTtJCxPoEr5Y"
DATE = "2026-11-22"

e = html.escape

# ---------------------------------------------------------------- contenus
SERVICES = [
  dict(slug="vitrier-urgence-vitre-cassee", court="Urgence vitre cassée", urgent=True,
    titre="Vitrier d'urgence à Rosny-sous-Bois, vitre cassée 24h/24",
    h1="Vitre cassée ? Vitrier d'urgence 24h/24",
    desc="Vitre ou double vitrage cassé à Rosny-sous-Bois et en Île-de-France : mise en sécurité 24h/24, remplacement du verre, devis immédiat. Appelez le 07 83 38 68 24.",
    carte="Mise en sécurité et remplacement de vitre, vitrine ou double vitrage, de jour comme de nuit.",
    intro="Une vitre brisée après une effraction, un choc ou une tempête ne peut pas attendre. Nous intervenons 24h/24 et 7j/7 pour sécuriser votre logement ou votre commerce, puis remplacer le verre aux bonnes dimensions.",
    blocs=[("Ce que nous faisons", ["Mise en sécurité immédiate de l'ouverture","Remplacement de simple vitrage, double vitrage et verre feuilleté de sécurité","Remplacement de vitrine de commerce","Évacuation des débris et nettoyage après intervention"]),
           ("Comment ça se passe", ["Vous appelez ou envoyez une photo par SMS au 07 83 38 68 24","Nous vous donnons un devis immédiat","Nous sécurisons sur place, puis posons le verre neuf, souvent le jour même quand c'est possible"])],
    faq=[("Intervenez-vous la nuit et le week-end ?","Oui. Nous répondons 24h/24 et 7j/7, y compris les dimanches et jours fériés."),
         ("Pouvez-vous remplacer seulement le verre sans changer la fenêtre ?","Oui, dans la grande majorité des cas. Nous gardons le cadre et posons un verre neuf aux mesures exactes."),
         ("Faites-vous un devis pour mon assurance ?","Oui. Nous établissons un devis détaillé que vous pouvez transmettre à votre assureur pour un sinistre bris de glace.")],
    image="avant-apres-vitre-cassee"),
  dict(slug="miroir-sur-mesure", court="Miroirs et crédences",
    titre="Miroir sur mesure et crédence en verre à Rosny-sous-Bois",
    h1="Miroirs sur mesure et crédences en verre",
    desc="Miroirs sur mesure ronds, ovales ou rectangulaires, miroirs muraux et crédences en verre laqué, découpés et posés chez vous en Île-de-France. Devis immédiat.",
    carte="Ronds, ovales ou rectangulaires, découpés à vos mesures et posés chez vous. Crédences en verre laqué.",
    intro="Un miroir bien posé agrandit une pièce et apporte de la lumière. Nous découpons et façonnons vos miroirs à la forme et aux dimensions voulues, puis nous les posons solidement, de la salle de bain au mur entier.",
    blocs=[("Nos réalisations en miroiterie", ["Miroirs de salle de bain, d'entrée ou de dressing","Miroirs muraux grande taille et murs de miroirs","Miroirs ronds, ovales ou de forme sur mesure, bords façonnés","Remplacement d'un miroir cassé ou piqué","Crédences de cuisine en verre laqué, faciles à nettoyer"]),
           ("Pour les professionnels", ["Salles de sport, salons de coiffure, studios de danse","Commerces et agences, chantiers d'architectes"])],
    faq=[("Pouvez-vous poser un miroir sur un mur entier ?","Oui. Nous prenons les mesures sur place et posons un ou plusieurs miroirs jointifs, collés et fixés selon le support."),
         ("Quelle couleur pour une crédence en verre ?","Le verre laqué existe dans de nombreuses teintes. Nous vous conseillons selon votre cuisine lors du devis.")],
    image="avant-apres-miroir-ovale"),
  dict(slug="paroi-de-douche-sur-mesure", court="Parois de douche",
    titre="Paroi de douche sur mesure en verre à Rosny-sous-Bois",
    h1="Parois de douche et pare-baignoire sur mesure",
    desc="Pose de parois de douche fixes, battantes ou coulissantes et de pare-baignoire en verre trempé, sur mesure, en Île-de-France. Devis immédiat au 07 83 38 68 24.",
    carte="Parois fixes, battantes ou coulissantes, pare-baignoire, en verre trempé.",
    intro="Une niche de douche hors standard, une salle de bain à rénover ou une paroi cassée à remplacer : nous posons des parois de douche adaptées à vos mesures, avec une quincaillerie solide et des joints étanches.",
    blocs=[("Les solutions", ["Paroi fixe type « walk-in » avec barre de stabilisation","Porte battante sur charnières murales","Porte coulissante pour les petites salles de bain","Pare-baignoire fixe ou pivotant","Verre trempé de sécurité, transparent ou dépoli"]),
           ("Nos conseils", ["Nous mesurons la niche au millimètre, car les murs sont rarement droits","Nous vous indiquons le sens d'ouverture le plus pratique avant la commande"])],
    faq=[("Ma niche de douche n'a pas une taille standard, est-ce possible ?","Oui. Nous adaptons la paroi à vos mesures, avec des profilés de réglage ou du verre sur mesure."),
         ("Remplacez-vous une paroi de douche cassée ?","Oui. Nous remplaçons le verre ou la paroi complète, et nous pouvons faire le devis pour votre assurance.")],
    image=None),
  dict(slug="fenetres-double-vitrage-volets", court="Fenêtres et volets",
    titre="Fenêtres, double vitrage et volets roulants à Rosny-sous-Bois",
    h1="Fenêtres, double vitrage et volets roulants",
    desc="Fourniture et pose de fenêtres PVC et alu, portes-fenêtres, baies vitrées, remplacement de double vitrage, volets roulants et portes Clarit en Île-de-France.",
    carte="Fourniture et pose, remplacement de double vitrage, volets roulants, portes Clarit.",
    intro="Des fenêtres qui ferment mal ou un simple vitrage qui laisse passer le froid : nous remplaçons vos menuiseries ou seulement le vitrage, pour gagner en confort et en isolation.",
    blocs=[("Fenêtres et portes", ["Fenêtres et portes-fenêtres PVC ou aluminium, en rénovation ou à neuf","Baies vitrées coulissantes","Passage du simple au double vitrage","Portes Clarit sur mesure"]),
           ("Volets roulants", ["Volets roulants manuels, électriques ou solaires","Remplacement de treuil, de sangle ou de moteur"]),
           ("Petits plus", ["Pose d'une chatière dans une vitre, en simple ou double vitrage, sans changer la fenêtre"])],
    faq=[("Peut-on passer au double vitrage sans changer la fenêtre ?","Souvent oui, si le cadre est en bon état et assez profond. Sinon, nous vous proposons une fenêtre de rénovation posée sur l'ancien dormant."),
         ("Pouvez-vous installer une chatière dans un double vitrage ?","Oui. Nous fabriquons un double vitrage percé au diamètre de la chatière, l'isolation est conservée.")],
    image="avant-apres-baie-vitree"),
  dict(slug="verriere-marquise-vitrage", court="Verrières et marquises",
    titre="Remplacement de verre de verrière et marquise à Rosny-sous-Bois",
    h1="Verrières et marquises : remplacement des verres",
    desc="Remplacement des verres cassés ou abîmés de verrière, marquise et véranda, en gardant votre armature existante. Rosny-sous-Bois et Île-de-France.",
    carte="Remplacement des verres en gardant votre armature existante.",
    intro="Votre verrière ou votre marquise a un verre fêlé, cassé ou opaque ? Nous remplaçons les vitrages en conservant la structure existante, ce qui coûte bien moins cher qu'un remplacement complet.",
    blocs=[("Ce que nous remplaçons", ["Verres de verrière d'atelier intérieure","Verres de marquise au-dessus d'une porte d'entrée","Vitrages de véranda","Verre feuilleté ou armé pour les toitures vitrées"])],
    faq=[("Fournissez-vous l'armature de la verrière ?","Non. Nous remplaçons les verres et gardons votre structure existante.")],
    image=None),
  dict(slug="serrurerie-reglage-cremone", court="Serrurerie et réglages",
    titre="Réglage de fenêtre et remplacement de crémone à Rosny-sous-Bois",
    h1="Serrurerie : réglage de fenêtres et crémones",
    desc="Fenêtre ou porte-fenêtre qui ferme mal, crémone cassée, porte bloquée : réglage et remplacement de crémones et de quincaillerie à Rosny-sous-Bois et en Île-de-France.",
    carte="Réglage et remplacement de crémones, portes et fenêtres qui ferment mal.",
    intro="Une poignée qui force, une fenêtre oscillo-battante qui se décroche ou une porte-fenêtre bloquée ouverte : souvent, un réglage ou le remplacement de la crémone suffit, sans changer la fenêtre.",
    blocs=[("Nos interventions", ["Réglage de fenêtres et portes-fenêtres PVC, alu et bois","Remplacement de crémone, de poignée et de gâches","Transformation d'une fenêtre à la française en oscillo-battante","Dépannage de porte-fenêtre bloquée, même la nuit"])],
    faq=[("Ma fenêtre ne ferme plus, faut-il la changer ?","Rarement. Dans la plupart des cas, un réglage ou une crémone neuve règle le problème pour bien moins cher.")],
    image="avant-apres-porte-fenetre"),
]

VILLES = [
  dict(slug="vitrier-montreuil", nom="Montreuil", cp="93100", voisines=["Bagnolet","Fontenay-sous-Bois","Romainville","Rosny-sous-Bois"],
       texte="Montreuil est juste à côté de Rosny-sous-Bois. Entre ses immeubles, ses maisons de ville et ses anciens ateliers, on y trouve beaucoup de verrières et de grandes surfaces vitrées : nous remplaçons les verres en gardant la structure.",
       detail="Du Bas-Montreuil aux quartiers du haut, nous posons aussi des miroirs sur mesure, des crédences et des parois de douche dans les appartements rénovés.",
       q=("Remplacez-vous les verres d'une verrière d'atelier à Montreuil ?","Oui. Nous mesurons chaque carreau, coupons les verres à la bonne taille et les posons dans l'armature existante, sans la changer.")),
  dict(slug="vitrier-noisy-le-sec", nom="Noisy-le-Sec", cp="93130", voisines=["Bondy","Romainville","Rosny-sous-Bois"],
       texte="Noisy-le-Sec est limitrophe de Rosny-sous-Bois. Pour une vitre cassée, une fenêtre qui ferme mal ou un miroir sur mesure, nous sommes à quelques minutes.",
       detail="Pavillons, immeubles et commerces : nous remplaçons les doubles vitrages fendus et réglons les fenêtres et portes-fenêtres qui frottent ou ferment mal.",
       q=("Pouvez-vous régler une fenêtre qui ferme mal à Noisy-le-Sec ?","Oui. Souvent un réglage ou le remplacement de la crémone suffit, sans changer la fenêtre.")),
  dict(slug="vitrier-villemomble", nom="Villemomble", cp="93250", voisines=["Le Raincy","Gagny","Rosny-sous-Bois"],
       texte="Villemomble touche Rosny-sous-Bois. Maisons individuelles et pavillons y sont nombreux : nous y posons fenêtres, volets roulants et portes-fenêtres, et remplaçons les verres de verrières et marquises.",
       detail="Pour les maisons, nous proposons aussi les volets roulants solaires, sans câble à tirer jusqu'au tableau électrique.",
       q=("Posez-vous des volets roulants à Villemomble ?","Oui : manuels, électriques ou solaires, fournis et posés sur vos fenêtres existantes ou neuves.")),
  dict(slug="vitrier-bondy", nom="Bondy", cp="93140", voisines=["Noisy-le-Sec","Les Pavillons-sous-Bois","Rosny-sous-Bois"],
       texte="Bondy est à quelques minutes de notre base de Rosny-sous-Bois. Particuliers, commerces et bailleurs nous appellent pour sécuriser une vitre cassée ou remplacer un vitrage.",
       detail="Après un bris de glace ou une effraction, nous mettons d'abord les lieux en sécurité, puis nous posons le verre neuf aux bonnes mesures.",
       q=("Remplacez-vous les vitrines de commerce à Bondy ?","Oui. Nous sécurisons la vitrine cassée puis posons un verre neuf adapté, feuilleté si besoin.")),
  dict(slug="vitrier-bagnolet", nom="Bagnolet", cp="93170", voisines=["Montreuil","Romainville","Paris 20e"],
       texte="Bagnolet est proche de Rosny-sous-Bois et des portes de Paris. Nous y remplaçons vitres, vitrines et doubles vitrages, et nous posons parois de douche et miroirs sur mesure.",
       detail="Dans les immeubles comme dans les maisons, nous remplaçons un seul vitrage sans toucher au cadre quand la menuiserie est en bon état.",
       q=("Peut-on changer seulement le double vitrage à Bagnolet ?","Oui. Si le cadre est en bon état, nous remplaçons uniquement le vitrage, ce qui coûte moins cher qu'une fenêtre neuve.")),
  dict(slug="vitrier-fontenay-sous-bois", nom="Fontenay-sous-Bois", cp="94120", voisines=["Vincennes","Montreuil","Rosny-sous-Bois"],
       texte="Fontenay-sous-Bois, dans le Val-de-Marne, est voisine de Rosny-sous-Bois. Nous y intervenons pour les urgences comme pour les projets de miroirs, de parois de douche et de fenêtres.",
       detail="Pour une salle de bain, nous prenons les mesures sur place et posons une paroi de douche ou un pare-baignoire adapté à votre espace.",
       q=("Posez-vous des parois de douche sur mesure à Fontenay-sous-Bois ?","Oui : parois fixes ou coulissantes et pare-baignoire, mesurés chez vous puis posés.")),
  dict(slug="vitrier-vincennes", nom="Vincennes", cp="94300", voisines=["Fontenay-sous-Bois","Saint-Mandé","Montreuil","Paris 12e et 20e"],
       texte="À Vincennes, beaucoup d'appartements anciens ont de grandes fenêtres, des miroirs muraux et des salles de bain à rénover. Nous posons miroirs sur mesure, parois de douche et remplaçons les vitrages.",
       detail="Un miroir au-dessus d'une cheminée ou sur tout un mur : nous le découpons à vos mesures et le posons proprement.",
       q=("Faites-vous des miroirs sur mesure à Vincennes ?","Oui : ronds, ovales ou rectangulaires, à vos mesures, fournis et posés chez vous.")),
  dict(slug="vitrier-romainville", nom="Romainville", cp="93230", voisines=["Noisy-le-Sec","Bagnolet","Les Lilas","Montreuil"],
       texte="Romainville, entre Noisy-le-Sec et Bagnolet, mêle pavillons et immeubles récents. Nous y intervenons pour les vitres cassées, les doubles vitrages et les fenêtres qui ferment mal.",
       detail="Dans les logements neufs comme anciens, nous posons aussi crédences en verre et miroirs sur mesure.",
       q=("Posez-vous des crédences en verre à Romainville ?","Oui. Nous posons des crédences en verre laqué, découpées aux mesures de votre cuisine.")),
  dict(slug="vitrier-gagny", nom="Gagny", cp="93220", voisines=["Villemomble","Le Raincy","Neuilly-sur-Marne","Montfermeil"],
       texte="Gagny est une ville surtout résidentielle, avec beaucoup de maisons. Nous y remplaçons fenêtres, portes-fenêtres et volets roulants, et réparons les vitres cassées.",
       detail="Pour une maison, nous pouvons changer une seule fenêtre ou toutes les menuiseries, avec un devis immédiat.",
       q=("Remplacez-vous toutes les fenêtres d'une maison à Gagny ?","Oui. Nous fournissons et posons fenêtres et portes-fenêtres, une seule ou toute la maison.")),
  dict(slug="vitrier-le-raincy", nom="Le Raincy", a="au Raincy", cp="93340", voisines=["Villemomble","Gagny","Livry-Gargan","Clichy-sous-Bois"],
       texte="Au Raincy, beaucoup de maisons anciennes ont des marquises, des verrières et des portes vitrées. Nous remplaçons les verres en gardant les ferronneries d'origine.",
       detail="Verre cathédrale, verre feuilleté ou verre armé : nous choisissons avec vous le verre qui respecte le style de la maison.",
       q=("Remplacez-vous les verres d'une marquise ancienne au Raincy ?","Oui. Nous déposons les anciens verres et posons des verres neufs à l'identique dans l'armature existante.")),
  dict(slug="vitrier-neuilly-plaisance", nom="Neuilly-Plaisance", cp="93360", voisines=["Rosny-sous-Bois","Neuilly-sur-Marne","Le Perreux-sur-Marne","Villemomble"],
       texte="Neuilly-Plaisance partage le plateau d'Avron avec Rosny-sous-Bois : nous sommes tout près. Nous y intervenons pour les vitres cassées, les fenêtres et les volets roulants.",
       detail="Des bords de Marne au plateau, nous réglons et remplaçons aussi les crémones des fenêtres qui ne ferment plus.",
       q=("Intervenez-vous vite à Neuilly-Plaisance ?","Neuilly-Plaisance est voisine de Rosny-sous-Bois, notre base. Appelez-nous, nous vous disons tout de suite quand nous pouvons passer.")),
  dict(slug="vitrier-neuilly-sur-marne", nom="Neuilly-sur-Marne", cp="93330", voisines=["Neuilly-Plaisance","Gagny","Noisy-le-Grand"],
       texte="À Neuilly-sur-Marne, nous intervenons dans les pavillons comme dans les résidences pour remplacer vitres et doubles vitrages, et poser fenêtres et volets roulants.",
       detail="Pour les copropriétés et les bailleurs, nous remplaçons aussi les vitrages des parties communes.",
       q=("Travaillez-vous pour les copropriétés à Neuilly-sur-Marne ?","Oui. Nous intervenons pour les syndics, les agences et les bailleurs, sur les logements comme sur les parties communes.")),
  dict(slug="vitrier-le-perreux-sur-marne", nom="Le Perreux-sur-Marne", a="au Perreux-sur-Marne", cp="94170", voisines=["Nogent-sur-Marne","Neuilly-Plaisance","Bry-sur-Marne","Fontenay-sous-Bois"],
       texte="Le Perreux-sur-Marne compte beaucoup de maisons et de villas. Nous y posons miroirs sur mesure, parois de douche, fenêtres et volets roulants.",
       detail="Pour une maison ancienne, nous pouvons aussi remplacer les verres d'une véranda ou d'une verrière.",
       q=("Remplacez-vous un verre de véranda au Perreux-sur-Marne ?","Oui. Nous mesurons le verre abîmé et posons un verre neuf adapté dans la structure existante.")),
  dict(slug="vitrier-nogent-sur-marne", nom="Nogent-sur-Marne", cp="94130", voisines=["Le Perreux-sur-Marne","Fontenay-sous-Bois","Vincennes","Joinville-le-Pont"],
       texte="À Nogent-sur-Marne, entre appartements anciens et maisons des bords de Marne, nous remplaçons les vitrages et posons miroirs, crédences et parois de douche.",
       detail="Pour une salle de bain ou une cuisine à rénover, nous venons prendre les mesures et vous donnons un devis immédiat.",
       q=("Venez-vous prendre les mesures à Nogent-sur-Marne ?","Oui. Pour un miroir, une crédence ou une paroi de douche, nous mesurons chez vous avant de fabriquer.")),
  dict(slug="vitrier-noisy-le-grand", nom="Noisy-le-Grand", cp="93160", voisines=["Neuilly-sur-Marne","Bry-sur-Marne","Champs-sur-Marne"],
       texte="À Noisy-le-Grand, nous intervenons pour les particuliers, les commerces et les bureaux : vitre cassée, vitrine, double vitrage, miroirs et parois de douche.",
       detail="Après une casse dans un commerce ou un bureau, nous mettons les lieux en sécurité puis posons le verre neuf.",
       q=("Intervenez-vous pour les bureaux et commerces à Noisy-le-Grand ?","Oui. Nous remplaçons vitrines, portes vitrées et vitrages de bureaux, et mettons les lieux en sécurité après une casse.")),
  dict(slug="vitrier-paris", nom="Paris", cp="75", voisines=["Paris 11e","Paris 12e","Paris 19e","Paris 20e"],
       texte="Depuis Rosny-sous-Bois, nous intervenons dans tout Paris, et surtout dans l'est : 11e, 12e, 19e et 20e arrondissements. Vitres cassées, doubles vitrages, miroirs et crédences.",
       detail="Dans les appartements anciens, nous posons miroirs sur mesure et parois de douche, et remplaçons les verres de verrières d'atelier.",
       q=("Intervenez-vous dans tout Paris ?","Oui, dans tous les arrondissements, et surtout dans l'est parisien, proche de notre base de Rosny-sous-Bois.")),
]

# Arrondissements de Paris (demande de Dwinter le 23/11/2026 : « tout Paris »), reliés depuis la page Paris
ARRONDISSEMENTS = [
  dict(slug="vitrier-paris-1er", nom="Paris 1er", cp="75001", parent="vitrier-paris", voisines=['Paris 2e', 'Paris 4e', 'Paris 8e'],
       texte='Nous intervenons dans le 1er arrondissement, au cœur de Paris, autour du Louvre, de Châtelet, des Halles et du Palais-Royal. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Beaucoup de commerces et de vitrines : après une casse, nous mettons la vitrine en sécurité puis posons le verre neuf.',
       q=('Remplacez-vous une vitrine cassée dans le 1er arrondissement ?', 'Oui. Nous sécurisons la vitrine, puis nous posons un verre neuf adapté, feuilleté si besoin.')),
  dict(slug="vitrier-paris-2e", nom="Paris 2e", cp="75002", parent="vitrier-paris", voisines=['Paris 1er', 'Paris 3e', 'Paris 9e'],
       texte='Nous intervenons dans le 2e arrondissement, du Sentier à la Bourse, avec ses passages couverts et ses immeubles de bureaux. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Bureaux, ateliers et appartements anciens : nous remplaçons vitrages et portes vitrées, et posons des miroirs sur mesure.',
       q=('Intervenez-vous dans les bureaux du 2e arrondissement ?', 'Oui. Nous remplaçons les vitrages, les portes vitrées et les cloisons en verre des bureaux et des commerces.')),
  dict(slug="vitrier-paris-3e", nom="Paris 3e", cp="75003", parent="vitrier-paris", voisines=['Paris 2e', 'Paris 4e', 'Paris 10e', 'Paris 11e'],
       texte="Nous intervenons dans le 3e arrondissement, dans le Haut-Marais et autour des Arts-et-Métiers, entre anciens ateliers et immeubles d'époque. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail="Les anciens ateliers ont souvent des verrières : nous changeons les verres en gardant la structure d'origine.",
       q=("Changez-vous les verres d'une verrière dans le 3e arrondissement ?", "Oui. Nous mesurons chaque carreau et posons les verres neufs dans l'armature existante.")),
  dict(slug="vitrier-paris-4e", nom="Paris 4e", cp="75004", parent="vitrier-paris", voisines=['Paris 1er', 'Paris 3e', 'Paris 5e', 'Paris 11e', 'Paris 12e'],
       texte="Nous intervenons dans le 4e arrondissement, dans le Marais, sur l'île Saint-Louis et l'île de la Cité, autour de l'Hôtel de Ville. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail='Les immeubles anciens ont des fenêtres à petits carreaux : nous remplaçons un carreau cassé sans changer la fenêtre.',
       q=('Peut-on remplacer un seul petit carreau dans le 4e arrondissement ?', "Oui. Nous coupons le verre à la mesure du carreau et le posons dans la fenêtre d'origine.")),
  dict(slug="vitrier-paris-5e", nom="Paris 5e", cp="75005", parent="vitrier-paris", voisines=['Paris 4e', 'Paris 6e', 'Paris 13e', 'Paris 14e'],
       texte='Nous intervenons dans le 5e arrondissement, dans le Quartier latin, autour du Panthéon, de la rue Mouffetard et du Jardin des Plantes. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Appartements anciens et logements étudiants : vitre cassée, fenêtre qui ferme mal ou miroir de salle de bain, nous intervenons.',
       q=('Réglez-vous les fenêtres anciennes dans le 5e arrondissement ?', "Oui. Un réglage ou une crémone neuve suffit souvent pour qu'une fenêtre ferme bien à nouveau.")),
  dict(slug="vitrier-paris-6e", nom="Paris 6e", cp="75006", parent="vitrier-paris", voisines=['Paris 5e', 'Paris 7e', 'Paris 14e', 'Paris 15e'],
       texte="Nous intervenons dans le 6e arrondissement, à Saint-Germain-des-Prés, à l'Odéon et autour du jardin du Luxembourg. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail='Galeries, boutiques et appartements : nous posons miroirs sur mesure, crédences en verre et remplaçons les vitrines.',
       q=('Posez-vous des miroirs sur mesure dans le 6e arrondissement ?', "Oui : miroirs muraux, au-dessus d'une cheminée ou de salle de bain, découpés à vos mesures et posés chez vous.")),
  dict(slug="vitrier-paris-7e", nom="Paris 7e", cp="75007", parent="vitrier-paris", voisines=['Paris 6e', 'Paris 15e', 'Paris 8e'],
       texte='Nous intervenons dans le 7e arrondissement, autour des Invalides, du Champ-de-Mars et du Gros-Caillou. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Les grands appartements ont souvent de hautes fenêtres et des miroirs muraux : nous remplaçons les vitrages et posons des miroirs à vos mesures.',
       q=('Remplacez-vous les vitrages de grandes fenêtres dans le 7e arrondissement ?', 'Oui. Nous mesurons sur place et posons des vitrages neufs, simples ou doubles, dans vos fenêtres existantes.')),
  dict(slug="vitrier-paris-8e", nom="Paris 8e", cp="75008", parent="vitrier-paris", voisines=['Paris 1er', 'Paris 9e', 'Paris 16e', 'Paris 17e'],
       texte='Nous intervenons dans le 8e arrondissement, des Champs-Élysées à la Madeleine et au parc Monceau, entre bureaux, boutiques et appartements. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Pour les bureaux et les boutiques, nous remplaçons portes vitrées, vitrines et cloisons en verre.',
       q=('Intervenez-vous pour les boutiques du 8e arrondissement ?', 'Oui. Nous remplaçons vitrines et portes vitrées, et mettons les lieux en sécurité après une casse.')),
  dict(slug="vitrier-paris-9e", nom="Paris 9e", cp="75009", parent="vitrier-paris", voisines=['Paris 2e', 'Paris 8e', 'Paris 10e', 'Paris 18e'],
       texte="Nous intervenons dans le 9e arrondissement, autour de l'Opéra, de la Nouvelle Athènes et de la rue des Martyrs. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail='Immeubles anciens et appartements rénovés : miroirs, crédences, parois de douche et doubles vitrages.',
       q=('Posez-vous des parois de douche dans le 9e arrondissement ?', 'Oui : parois fixes ou coulissantes et pare-baignoire, mesurés chez vous puis posés.')),
  dict(slug="vitrier-paris-10e", nom="Paris 10e", cp="75010", parent="vitrier-paris", voisines=['Paris 3e', 'Paris 9e', 'Paris 11e', 'Paris 19e'],
       texte="Nous intervenons dans le 10e arrondissement, le long du canal Saint-Martin et autour des gares du Nord et de l'Est. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail='Commerces, ateliers et appartements : nous intervenons vite pour une vitre cassée et remplaçons les doubles vitrages.',
       q=('Intervenez-vous la nuit dans le 10e arrondissement ?', 'Oui. Nous répondons 24h/24 et 7j/7 pour sécuriser une vitre ou une vitrine cassée.')),
  dict(slug="vitrier-paris-11e", nom="Paris 11e", cp="75011", parent="vitrier-paris", voisines=['Paris 12e', 'Paris 20e', 'Paris 3e', 'Paris 10e'],
       texte="Nous intervenons dans le 11e arrondissement, de la Bastille à République, d'Oberkampf à la rue de la Roquette. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail="Les cours d'artisans du 11e ont beaucoup d'ateliers vitrés et de verrières : nous remplaçons les verres en gardant la structure.",
       q=('Venez-vous vite dans le 11e arrondissement ?', "Le 11e est dans l'est parisien, proche de notre base de Rosny-sous-Bois. Appelez-nous, nous vous disons tout de suite quand nous pouvons passer.")),
  dict(slug="vitrier-paris-12e", nom="Paris 12e", cp="75012", parent="vitrier-paris", voisines=['Paris 11e', 'Paris 20e', 'Vincennes', 'Saint-Mandé'],
       texte='Nous intervenons dans le 12e arrondissement, de Bercy à Nation, de la Bastille au bois de Vincennes. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Le 12e touche Vincennes et Saint-Mandé, sur notre route depuis Rosny-sous-Bois : vitres cassées, fenêtres, miroirs et volets roulants.',
       q=('Posez-vous des volets roulants dans le 12e arrondissement ?', 'Oui : manuels, électriques ou solaires, fournis et posés sur vos fenêtres.')),
  dict(slug="vitrier-paris-13e", nom="Paris 13e", cp="75013", parent="vitrier-paris", voisines=['Paris 5e', 'Paris 12e', 'Paris 14e'],
       texte='Nous intervenons dans le 13e arrondissement, de la Butte-aux-Cailles au quartier des Olympiades et à Paris Rive Gauche. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Tours, résidences et immeubles récents : nous remplaçons doubles vitrages et réglons les fenêtres et portes-fenêtres.',
       q=('Remplacez-vous les doubles vitrages en immeuble dans le 13e arrondissement ?', 'Oui. Nous remplaçons le vitrage sans changer la fenêtre quand le cadre est en bon état.')),
  dict(slug="vitrier-paris-14e", nom="Paris 14e", cp="75014", parent="vitrier-paris", voisines=['Paris 6e', 'Paris 13e', 'Paris 15e'],
       texte="Nous intervenons dans le 14e arrondissement, de Montparnasse à Alésia et Denfert-Rochereau, avec ses ateliers d'artistes. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail="Les ateliers d'artistes ont de grandes surfaces vitrées : nous remplaçons les verres abîmés à la bonne mesure.",
       q=("Remplacez-vous les grandes vitres d'atelier dans le 14e arrondissement ?", 'Oui. Nous mesurons sur place et posons les verres neufs dans la structure existante.')),
  dict(slug="vitrier-paris-15e", nom="Paris 15e", cp="75015", parent="vitrier-paris", voisines=['Paris 7e', 'Paris 14e', 'Paris 16e'],
       texte='Nous intervenons dans le 15e arrondissement, de Vaugirard à Grenelle, de Convention à Beaugrenelle. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Le 15e est très résidentiel : nous y posons miroirs, crédences et parois de douche, et remplaçons les vitrages.',
       q=('Posez-vous des crédences en verre dans le 15e arrondissement ?', 'Oui. Nous posons des crédences en verre laqué, découpées aux mesures de votre cuisine.')),
  dict(slug="vitrier-paris-16e", nom="Paris 16e", cp="75016", parent="vitrier-paris", voisines=['Paris 8e', 'Paris 15e', 'Paris 17e'],
       texte='Nous intervenons dans le 16e arrondissement, à Passy, Auteuil et autour du Trocadéro. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail='Grands appartements et hôtels particuliers : miroirs sur mesure, grandes fenêtres, portes vitrées et verrières.',
       q=('Faites-vous les grands miroirs muraux dans le 16e arrondissement ?', 'Oui. Nous découpons le miroir à vos mesures et le posons, même sur tout un mur.')),
  dict(slug="vitrier-paris-17e", nom="Paris 17e", cp="75017", parent="vitrier-paris", voisines=['Paris 8e', 'Paris 16e', 'Paris 18e'],
       texte="Nous intervenons dans le 17e arrondissement, des Batignolles aux Ternes, jusqu'au quartier Clichy-Batignolles. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail='Immeubles anciens et logements neufs : vitres cassées, doubles vitrages, miroirs et parois de douche.',
       q=('Intervenez-vous dans les immeubles neufs du 17e arrondissement ?', "Oui. Nous intervenons sur les vitrages, fenêtres et parois de douche, dans le neuf comme dans l'ancien.")),
  dict(slug="vitrier-paris-18e", nom="Paris 18e", cp="75018", parent="vitrier-paris", voisines=['Paris 9e', 'Paris 17e', 'Paris 19e'],
       texte="Nous intervenons dans le 18e arrondissement, de Montmartre à la Goutte d'Or et à Lamarck. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.",
       detail="Sur la butte, beaucoup d'immeubles anciens ont des fenêtres et des portes vitrées d'origine : nous remplaçons les verres sans changer la menuiserie.",
       q=('Remplacez-vous les verres de porte vitrée dans le 18e arrondissement ?', 'Oui : verre clair, dépoli ou cathédrale, coupé à la mesure et posé dans votre porte.')),
  dict(slug="vitrier-paris-19e", nom="Paris 19e", cp="75019", parent="vitrier-paris", voisines=['Paris 10e', 'Paris 20e', 'Paris 18e'],
       texte='Nous intervenons dans le 19e arrondissement, des Buttes-Chaumont à La Villette et au bassin de la Villette. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail="Le 19e est dans l'est parisien, proche de notre secteur : vitres cassées, doubles vitrages, volets roulants et réglages de fenêtres.",
       q=('Réglez-vous les portes-fenêtres qui ferment mal dans le 19e arrondissement ?', "Oui. Nous réglons la porte-fenêtre ou changeons la crémone pour qu'elle ferme bien.")),
  dict(slug="vitrier-paris-20e", nom="Paris 20e", cp="75020", parent="vitrier-paris", voisines=['Paris 11e', 'Paris 12e', 'Paris 19e', 'Bagnolet', 'Montreuil'],
       texte='Nous intervenons dans le 20e arrondissement, de Belleville à Ménilmontant, du Père-Lachaise à Gambetta. Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal : nous venons depuis Rosny-sous-Bois.',
       detail="Le 20e touche Bagnolet et Montreuil : c'est l'arrondissement le plus proche de notre base de Rosny-sous-Bois.",
       q=('Êtes-vous proches du 20e arrondissement ?', 'Oui. Le 20e touche Bagnolet et Montreuil, tout près de Rosny-sous-Bois : appelez-nous pour une intervention rapide.')),
]

SERVICES_ACCUEIL = [
  ("Urgence vitre cassée","Mise en sécurité et remplacement de vitre, vitrine ou double vitrage, de jour comme de nuit.",True),
  ("Miroirs sur mesure","Ronds, ovales ou rectangulaires, découpés à vos mesures et posés chez vous.",False),
  ("Crédences en verre","Verre laqué pour la cuisine, facile à nettoyer, posé proprement.",False),
  ("Parois de douche","Parois fixes ou coulissantes, pare-baignoire, sur mesure.",False),
  ("Marquises et verrières","Remplacement des verres en gardant votre armature existante.",False),
  ("Fenêtres et portes-fenêtres","Fourniture et pose, remplacement de double vitrage, portes Clarit.",False),
  ("Volets roulants","Manuels, électriques ou solaires, fournis et posés.",False),
  ("Serrurerie et réglages","Réglage et remplacement de crémones, portes, fenêtres et portes blindées qui ferment mal.",False),
]

# Pages villes en ligne (22/11/2026 : 4 villes ; 23/11/2026 : Dwinter demande toutes les villes de sa zone)
VILLES_PIED = [v["slug"] for v in VILLES]  # villes listées dans le pied de page (les 16 proches)
for v in VILLES: v["dep"] = DEP_EXISTANTES.get(v["slug"])
VILLES += NOUVELLES_VILLES  # villes principales des départements (23/11/2026)
VILLES_ACTIVES = [v["slug"] for v in VILLES]
DEP = {d["num"]: d for d in DEPARTEMENTS}

REALISATIONS = [
  ("avant-apres-vitre-cassee","Vitre cassée remplacée","La vitre était fendue et tenue par du ruban adhésif. Verre neuf coupé aux mesures et posé dans le cadre d'origine."),
  ("avant-apres-baie-vitree","Baie vitrée 4 vantaux","Remplacement d'une ancienne baie par une baie PVC blanc neuve."),
  ("avant-apres-porte-fenetre","Porte-fenêtre","Pose d'une porte-fenêtre PVC blanc neuve, finitions propres."),
  ("avant-apres-fenetre-pvc","Fenêtre 2 vantaux","Fenêtre remplacée par une fenêtre PVC blanc double vitrage."),
  ("avant-apres-miroir-ovale","Miroir ovale sur mesure","Miroir ovale façonné, fourni et posé dans une salle de bain."),
]

AVIS_CLIENTS = [  # (texte, prénom, mois) : avis Google 5 étoiles, prénom seulement
  ("Pose de deux portes-fenêtres et de volets solaires. Merci pour votre travail.","Jose","novembre 2026"),
  ("Remplacement de 4 doubles vitrages. Merci pour votre intervention.","Ti Goût Lakay","novembre 2026"),
  ("L'installation de ma fenêtre s'est très bien passée. Intervention rapide, efficace et soignée, avec un vrai professionnalisme. Le résultat est nickel !","Melinda","novembre 2026"),
  ("Dépannage d'urgence sur une porte-fenêtre bloquée en position ouverte : il est venu de nuit ! Hyper réactif et très professionnel.","Sarah","octobre 2026"),
]

FAQ_ACCUEIL = [
  ("Intervenez-vous 24h/24 ?","Oui. Pour une vitre cassée ou une fenêtre bloquée, nous répondons 24h/24 et 7j/7, y compris le week-end."),
  ("Dans quelles villes intervenez-vous ?","Nous sommes basés à Rosny-sous-Bois (93) et intervenons dans toute l'Île-de-France : Montreuil, Noisy-le-Sec, Villemomble, Bondy, Bagnolet, Fontenay-sous-Bois, Vincennes, Paris et bien d'autres."),
  ("Combien coûte un remplacement de vitre ?","Le prix dépend des dimensions, du type de verre et de l'accès. Envoyez-nous une photo par SMS : nous vous donnons un devis immédiat."),
  ("Travaillez-vous avec les assurances ?","Oui. Nous établissons un devis détaillé que vous transmettez à votre assureur en cas de bris de glace."),
  ("Travaillez-vous pour les professionnels ?","Oui : commerces, syndics, agences immobilières et architectes. Vitrines, miroirs et vitrages de locaux professionnels."),
]

ZONE = ["Rosny-sous-Bois","Montreuil","Noisy-le-Sec","Villemomble","Bondy","Bagnolet","Fontenay-sous-Bois","Vincennes","Romainville","Gagny","Le Raincy","Neuilly-Plaisance","Neuilly-sur-Marne","Le Perreux-sur-Marne","Nogent-sur-Marne","Noisy-le-Grand","Paris"]

# ---------------------------------------------------------------- briques
def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

ENTREPRISE = {
  "@context":"https://schema.org","@type":"HomeAndConstructionBusiness","@id":DOMAINE+"/#entreprise",
  "name":"Miroiterie Winter","description":"Vitrier, miroitier et serrurier à Rosny-sous-Bois, intervention 24h/24 en Île-de-France.",
  "url":DOMAINE+"/","telephone":"+33783386824","email":MAIL,
  "image":DOMAINE+"/images/avant-apres-vitre-cassee.jpg","logo":DOMAINE+"/images/icone-512.png",
  "address":{"@type":"PostalAddress","streetAddress":"141 rue du Général Leclerc","postalCode":"93110","addressLocality":"Rosny-sous-Bois","addressRegion":"Île-de-France","addressCountry":"FR"},
  "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}],
  "areaServed":[{"@type":"City","name":v} for v in ZONE] + [{"@type":"AdministrativeArea","name":"Île-de-France"}],
  "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":str(NB_AVIS),"bestRating":"5"},
  "hasMap":MAPS,"sameAs":[INSTAGRAM, MAPS],
}

def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":r}} for q,r in faq]}

def fil_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":DOMAINE+u} for i,(n,u) in enumerate(items)]}

ICON_TEL = '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>'
ICON_IG = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.9 8c0-1.6-.4-3-1.6-4.2S17.6 2.1 16 2.1C14.4 2 9.6 2 8 2.1c-1.6 0-3 .4-4.2 1.6S2.1 6.4 2.1 8C2 9.6 2 14.4 2.1 16c0 1.6.4 3 1.6 4.2s2.6 1.6 4.2 1.6c1.6.1 6.4.1 8 0 1.6 0 3-.4 4.2-1.6s1.6-2.6 1.6-4.2c.1-1.6.1-6.4 0-8zM19.8 18a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.3.4s-4.1.1-5.3-.4A3 3 0 0 1 5.8 18c-.5-1.2-.4-4-.4-5.3s-.1-4.1.4-5.3A3 3 0 0 1 7.5 5.7c1.2-.5 4-.4 5.3-.4s4.1-.1 5.3.4A3 3 0 0 1 19.8 7.4c.5 1.2.4 4 .4 5.3s.1 4.1-.4 5.3z"/></svg>'
ICON_MAP = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>'

def tete(titre, desc, chemin, ld=(), robots="index,follow", og_image="/images/avant-apres-vitre-cassee.jpg"):
    url = DOMAINE + chemin
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(titre)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<meta name="google-site-verification" content="3eZOdhtBjB0FbxQvSEV5quoKze304A2814nCYsD8Kec">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Miroiterie Winter">
<meta property="og:title" content="{e(titre)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAINE}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#16325f">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=Public+Sans:wght@400;600&display=swap">
<link rel="stylesheet" href="/style.css">
{"".join(jsonld(x) for x in ld)}
</head>
<body>
<a class="sauter" href="#contenu">Aller au contenu</a>
<header class="top"><div class="wrap">
  <a href="/" class="logo"><img src="/images/logo-entete.png" alt="Miroiterie Winter, vitrier serrurier" width="271" height="177"></a>
  <nav aria-label="Menu principal"><a href="/#services">Services</a><a href="/#avis">Avis</a><a href="/#zone">Zone</a><a href="/#faq">FAQ</a><a href="/#contact">Contact</a></nav>
  <a class="tel" href="{TEL_LIEN}">{ICON_TEL}<span>{TEL}</span></a>
</div></header>
<main id="contenu">
'''

def contact():
    return f'''<div class="contact" id="contact"><div class="wrap">
  <p class="eyebrow">Devis immédiat · 24h/24 · 7j/7</p>
  <a class="num" href="{TEL_LIEN}">{TEL}</a>
  <p><a class="mail" href="mailto:{MAIL}?subject=Demande%20de%20devis">{MAIL}</a> · {ADRESSE}</p>
  <p class="astuce">Astuce : envoyez une photo par SMS au {TEL} pour un devis encore plus rapide.</p>
  <a class="btn" href="{TEL_LIEN}">{ICON_TEL} Appeler Miroiterie Winter</a>
</div></div>
'''

def pied():
    return f'''</main>
{contact()}
<footer><div class="wrap">
  <div class="cols">
    <div><p class="ftitre">Miroiterie Winter</p><p>Vitrier, miroitier et serrurier à Rosny-sous-Bois (93), intervention 24h/24 dans toute l'Île-de-France.</p>
      <p class="reseaux"><a href="{INSTAGRAM}" rel="noopener" target="_blank" aria-label="Instagram Miroiterie Winter">{ICON_IG}<span>Instagram</span></a><a href="{MAPS}" rel="noopener" target="_blank" aria-label="Miroiterie Winter sur Google Maps">{ICON_MAP}<span>Google Maps</span></a></p>
      <p><a class="lien-avis" href="{AVIS}" rel="noopener" target="_blank">★ Laisser un avis Google</a></p></div>
    <div><p class="ftitre">Sur cette page</p><ul><li><a href="/#services">Nos services</a></li><li><a href="/#avis">Avis clients</a></li><li><a href="/#zone">Zone d'intervention</a></li><li><a href="/#faq">Questions fréquentes</a></li><li><a href="/#contact">Contact et devis</a></li></ul></div>
    <div><p class="ftitre">Villes</p><ul class="villes-pied"><li><a href="/">Vitrier Rosny-sous-Bois</a></li>{"".join(f'<li><a href="/{v["slug"]}/">Vitrier {e(v["nom"])}</a></li>' for v in VILLES if v["slug"] in VILLES_PIED)}</ul></div>
    <div><p class="ftitre">Départements</p><ul><li><a href="/vitrier-paris/">Vitrier Paris (75)</a></li>{"".join(f'<li><a href="/{d["slug"]}/">Vitrier {e(d["nom"])} ({d["num"]})</a></li>' for d in DEPARTEMENTS)}</ul></div>
  </div>
  <p class="legal">© 2026 Miroiterie Winter · Dwinter Morisseau, entrepreneur individuel · <a href="/mentions-legales/">Mentions légales</a></p>
</div></footer>
<a class="appel-fixe" href="{TEL_LIEN}">{ICON_TEL} Appeler · {TEL}</a>
<script src="/site.js" defer></script>
</body>
</html>
'''

def fil(items):
    li = "".join((f'<li><a href="{u}">{e(n)}</a></li>' if i < len(items)-1 else f'<li aria-current="page">{e(n)}</li>') for i,(n,u) in enumerate(items))
    return f'<nav class="fil" aria-label="Fil d\'Ariane"><ol>{li}</ol></nav>'

def bloc_faq(faq, titre="Questions fréquentes"):
    q = "".join(f'<details><summary>{e(a)}</summary><p>{e(b)}</p></details>' for a,b in faq)
    return f'<section class="faq" id="faq"><div class="wrap"><div><p class="eyebrow">FAQ</p><h2>{e(titre)}</h2></div><div class="faq-liste">{q}</div></div></section>'

def cartes_services():
    out = []
    for t, d, urgent in SERVICES_ACCUEIL:
        cls = ' class="urgent"' if urgent else ""
        out.append(f'<div{cls}><h3>{e(t)}</h3><p>{e(d)}</p></div>')
    return '<div class="services">' + "".join(out) + '</div>'

def zone_liens():
    liens = {v["nom"]: v["slug"] for v in VILLES if v["slug"] in VILLES_ACTIVES}
    return ", ".join(f'<a href="/{liens[z]}/">{e(z)}</a>' if z in liens else e(z) for z in ZONE)

def bloc_avis():
    fig = "".join(f'<figure><blockquote>«\u00a0{e(t)}\u00a0»</blockquote><figcaption><span class="stars" aria-label="5 étoiles">★★★★★</span> <span class="qui">{e(n)} · {m}</span></figcaption></figure>' for t,n,m in AVIS_CLIENTS)
    return f'''<section id="avis"><div class="wrap">
  <div class="score"><strong>{NOTE}</strong><span class="stars" aria-label="5 étoiles">★★★★★</span><span>{NB_AVIS} avis sur Google</span></div>
  <div class="reviews">{fig}</div>
  <p class="zone" id="zone"><b>Zone d'intervention :</b> {zone_liens()} et toute l'Île-de-France : {", ".join(f'<a href="/{d["slug"]}/">{e(d["nom"])} ({d["num"]})</a>' for d in DEPARTEMENTS)}.</p>
</div></section>'''

def hero(eyebrow, h1, lead, facts=True):
    f = f'''<div class="facts"><span><b>{NOTE} ★</b> {NB_AVIS} avis Google</span><span><b>24h/24</b> 7 jours sur 7</span><span><b>Devis</b> immédiat</span></div>''' if facts else ""
    return f'''<div class="hero"><div class="wrap">
  <p class="eyebrow">{e(eyebrow)}</p>
  <h1>{e(h1)}</h1>
  <p class="lead">{e(lead)}</p>
  <div class="row"><a class="btn" href="{TEL_LIEN}">{ICON_TEL} Appeler maintenant</a><a class="num" href="{TEL_LIEN}">{TEL}</a></div>
  {f}
</div></div>
'''

def img(nom, alt, lazy=True):
    return f'<img src="/images/{nom}.jpg" alt="{e(alt)}" width="800" height="1000"{" loading=\"lazy\"" if lazy else ""} decoding="async">'

def ecrire(chemin, contenu):
    contenu = contenu.replace(" ?", "\u00a0?").replace(" !", "\u00a0!")
    p = os.path.join(OUT, chemin.strip("/"), "index.html") if chemin != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(contenu)

PAGES = []

# ---------------------------------------------------------------- accueil
def page_accueil():
    ld = [ENTREPRISE, faq_ld(FAQ_ACCUEIL), {"@context":"https://schema.org","@type":"WebSite","name":"Miroiterie Winter","alternateName":["Miroiterie Winter Rosny-sous-Bois","miroiterie-winter.fr"],"url":DOMAINE+"/","publisher":{"@id":DOMAINE+"/#entreprise"}}]
    h = tete("Miroiterie Winter | Vitrier à Rosny-sous-Bois 24h/24", "Miroiterie Winter, vitrier à Rosny-sous-Bois (93) 24h/24 : vitre cassée, double vitrage, miroirs sur mesure, parois de douche, fenêtres. Devis immédiat au 07 83 38 68 24.", "/", ld)
    h += hero("Vitrier · Miroitier · Serrurier à Rosny-sous-Bois", "Vitre cassée ? On intervient 24h/24.",
              "Vitrier à Rosny-sous-Bois : urgence casse, miroirs sur mesure, crédences, parois de douche, fenêtres et volets. Devis immédiat et remplacement le jour même dès que possible, partout en Île-de-France.")
    h += f'''<section id="services"><div class="wrap">
  <div><p class="eyebrow">Nos services</p><h2>Verre, miroir, fenêtres et serrurerie</h2></div>
  {cartes_services()}
</div></section>
<section class="fond"><div class="wrap">
  <div class="proof">
    {img("avant-apres-vitre-cassee","Avant et après le remplacement d'une vitre cassée par Miroiterie Winter")}
    <div class="txt">
      <p class="eyebrow">Avant / après</p>
      <h2>Une vitre cassée remplacée</h2>
      <p>La vitre était fendue et tenue par du ruban adhésif. Nous avons coupé un verre neuf aux mesures et l'avons posé dans la fenêtre d'origine, sans toucher au cadre. Le chantier est laissé propre après notre passage.</p>
    </div>
  </div>
</div></section>
<section><div class="wrap atouts">
  <div><p class="eyebrow">Pourquoi nous appeler</p><h2>Un artisan local, joignable à toute heure</h2></div>
  <ul class="liste-atouts">
    <li><b>Basés à Rosny-sous-Bois</b> : nous connaissons le secteur et arrivons vite dans l'est parisien.</li>
    <li><b>24h/24 et 7j/7</b> : une vitre cassée la nuit ou le dimanche, nous répondons.</li>
    <li><b>Devis immédiat</b> : une photo par SMS suffit souvent pour vous donner un prix.</li>
    <li><b>Travail propre</b> : protection des lieux, évacuation des débris, nettoyage en fin de chantier.</li>
    <li><b>Particuliers et professionnels</b> : logements, commerces, syndics, agences et architectes.</li>
  </ul>
</div></section>
{bloc_avis()}
{bloc_faq(FAQ_ACCUEIL)}
'''
    h += pied()
    ecrire("/", h); PAGES.append(("/", "1.0"))

# ---------------------------------------------------------------- services
def page_service(s):
    chemin = f'/{s["slug"]}/'
    svc = {"@context":"https://schema.org","@type":"Service","name":s["h1"],"description":s["desc"],"provider":{"@id":DOMAINE+"/#entreprise"},"areaServed":"Île-de-France","url":DOMAINE+chemin}
    ld = [ENTREPRISE, svc, fil_ld([("Accueil","/"),(s["court"],chemin)])] + ([faq_ld(s["faq"])] if s.get("faq") else [])
    h = tete(s["titre"] + " | Miroiterie Winter" if len(s["titre"]) < 50 else s["titre"], s["desc"], chemin, ld,
             og_image=f'/images/{s["image"]}.jpg' if s.get("image") else "/images/avant-apres-vitre-cassee.jpg")
    h += '<div class="wrap">' + fil([("Accueil","/"),(s["court"],chemin)]) + '</div>'
    h += hero("Miroiterie Winter · Rosny-sous-Bois et Île-de-France", s["h1"], s["intro"])
    blocs = "".join(f'<div class="bloc"><h2>{e(t)}</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in l)}</ul></div>' for t,l in s["blocs"])
    visuel = f'<figure class="visuel">{img(s["image"], "Exemple de réalisation Miroiterie Winter : " + s["court"].lower())}</figure>' if s.get("image") else ""
    h += f'<section><div class="wrap"><div class="deux{" avec-image" if visuel else ""}"><div class="blocs">{blocs}</div>{visuel}</div></div></section>'
    if s.get("faq"): h += bloc_faq(s["faq"])
    autres = "".join(f'<a href="/{o["slug"]}/">{e(o["court"])}</a>' for o in SERVICES if o is not s)
    h += f'<section class="fond"><div class="wrap"><div><p class="eyebrow">Nos autres services</p><h2>Besoin d\'autre chose ?</h2></div><div class="villes">{autres}</div></div></section>'
    h += pied()
    ecrire(chemin, h); PAGES.append((chemin, "0.9"))

# ---------------------------------------------------------------- villes
def bloc_autres_villes(v, dep):
    if dep:
        proches = [o for o in VILLES if o.get("dep") == dep["num"] and o["slug"] != v["slug"]]
        tete = f'<a href="/{dep["slug"]}/">Vitrier {e(dep["nom"])} ({dep["num"]})</a>' + ('<a href="/">Vitrier Rosny-sous-Bois</a>' if dep["num"] == "93" else '')
        titre = f"Nous intervenons aussi {dep['de']}"
    else:
        proches = [o for o in VILLES if o["slug"] in VILLES_PIED and o["slug"] != v["slug"]]
        tete = '<a href="/">Vitrier Rosny-sous-Bois</a>'
        titre = "Nous intervenons aussi à"
    liens = "".join(f'<a href="/{o["slug"]}/">Vitrier {e(o["nom"])}</a>' for o in proches)
    return f'''<section class="fond"><div class="wrap"><div><p class="eyebrow">Autres villes</p><h2>{e(titre)}</h2></div><div class="villes">{tete}{liens}</div></div></section>'''

def page_departement(d):
    chemin = f'/{d["slug"]}/'
    villes = [o for o in VILLES if o.get("dep") == d["num"]]
    faq = [(f"Intervenez-vous partout {d['de']} ?", f"Oui. Nous intervenons dans toutes les communes {d['de']} ({d['num']}), pour les urgences comme pour les projets. Appelez-nous pour savoir quand nous pouvons passer."),
           (f"Comment obtenir un devis {d['de']} ?", f"Appelez le {TEL} ou envoyez une photo par SMS : nous vous donnons un devis immédiat.")]
    loc = {**ENTREPRISE, "areaServed":[{"@type":"AdministrativeArea","name":f"{d['nom']} ({d['num']})"}] + [{"@type":"City","name":o["nom"]} for o in villes]}
    ariane = [("Accueil","/"),(f"Vitrier {d['nom']}",chemin)]
    ld = [loc, fil_ld(ariane), faq_ld(faq)]
    titre = f"Vitrier {d['nom']} ({d['num']}) 24h/24 | Miroiterie Winter"
    if len(titre) > 60: titre = f"Vitrier {d['nom']} ({d['num']}) | Miroiterie Winter"
    desc = f"Vitrier {d['de']} ({d['num']}) 24h/24 : vitre cassée, double vitrage, miroirs, parois de douche, fenêtres. Devis immédiat au {TEL}."
    h = tete(titre, desc, chemin, ld)
    h += '<div class="wrap">' + fil(ariane) + '</div>'
    h += hero(f"Vitrier · Miroitier · Serrurier · {d['nom']} ({d['num']})", f"Vitrier {d['de']} ({d['num']}), 24h/24",
              f"Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal {d['de']} ? Miroiterie Winter, artisan basé à Rosny-sous-Bois, intervient avec un devis immédiat.")
    liens = ('<a href="/">Vitrier Rosny-sous-Bois</a>' if d["num"] == "93" else '') + "".join(f'<a href="/{o["slug"]}/">Vitrier {e(o["nom"])}</a>' for o in villes)
    h += f'''<section><div class="wrap">
  <div class="deux"><div class="bloc"><h2>Votre vitrier {e(d["de"])}</h2><p>{e(d["texte"])}</p>
  <p>Urgence vitre cassée 24h/24, remplacement de vitrage, miroirs sur mesure, crédences, parois de douche, verrières, fenêtres, volets roulants et réglage de crémones.</p></div>
  <div class="bloc"><h2>Nos villes {e(d["de"])}</h2><div class="villes">{liens}</div>
  <p>Et aussi : {e(", ".join(d["autres"]))}, et toutes les autres communes du {d["num"]}.</p></div></div>
</div></section>
{bloc_avis()}
{bloc_faq(faq, f"Vitrier {d['de']} : vos questions")}
<section class="fond"><div class="wrap"><div><p class="eyebrow">Île-de-France</p><h2>Nos autres départements</h2></div><div class="villes"><a href="/vitrier-paris/">Vitrier Paris (75)</a>{"".join(f'<a href="/{o["slug"]}/">Vitrier {e(o["nom"])} ({o["num"]})</a>' for o in DEPARTEMENTS if o is not d)}</div></div></section>
'''
    h += pied()
    ecrire(chemin, h); PAGES.append((chemin, "0.8"))

def bloc_arrondissements(v):
    liens = "".join(f'<a href="/{o["slug"]}/">Vitrier {e(o["nom"])}</a>' for o in ARRONDISSEMENTS if o is not v)
    retour = '' if v["slug"] == "vitrier-paris" else '<a href="/vitrier-paris/">Vitrier Paris</a><a href="/">Vitrier Rosny-sous-Bois</a>'
    return f'''<section class="fond"><div class="wrap"><div><p class="eyebrow">Paris</p><h2>Nous intervenons dans tous les arrondissements</h2></div><div class="villes">{retour}{liens}</div></div></section>'''

def page_ville(v):
    chemin = f'/{v["slug"]}/'
    n = v["nom"]
    an = v.get("a", "à " + n)  # « au Raincy », « au Perreux-sur-Marne »
    if "theme" in v:
        det, (qq, qr) = THEMES[v["theme"]]
        v = {**v, "detail": det, "q": (qq.format(an=an), qr)}
    dep = DEP.get(v.get("dep"))
    faq = [(f"Intervenez-vous en urgence {an} ?", f"Oui. Nous intervenons 24h/24 et 7j/7 {an} ({v['cp']}) pour sécuriser une vitre cassée et remplacer le vitrage, souvent le jour même quand c'est possible."),
           v["q"],
           (f"Comment obtenir un devis {an} ?", f"Appelez le {TEL} ou envoyez une photo par SMS : nous vous donnons un devis immédiat.")]
    loc = dict(ENTREPRISE); loc = {**ENTREPRISE, "areaServed":[{"@type":"City","name":n}] + [a for a in ENTREPRISE["areaServed"] if a["name"] != n]}
    ariane = [("Accueil","/")] + ([("Vitrier Paris","/vitrier-paris/")] if v.get("parent") else []) + ([(f"Vitrier {dep['nom']}", f"/{dep['slug']}/")] if dep else []) + [(f"Vitrier {n}",chemin)]
    ld = [loc, fil_ld(ariane), faq_ld(faq)]
    titre = f"Vitrier {n} ({v['cp']}) 24h/24 | Miroiterie Winter"
    if len(titre) > 60: titre = f"Vitrier {n} ({v['cp']}) | Miroiterie Winter"
    desc = f"Vitrier {an} ({v['cp']}) 24h/24 : vitre cassée, double vitrage, miroirs, parois de douche, fenêtres. Devis immédiat au {TEL}."
    h = tete(titre, desc, chemin, ld)
    h += '<div class="wrap">' + fil(ariane) + '</div>'
    h += hero(f"Vitrier · Miroitier · Serrurier {an}", f"Vitrier {an} ({v['cp']}), 24h/24",
              f"Vitre cassée, double vitrage, miroir ou fenêtre qui ferme mal {an} ? Miroiterie Winter, artisan basé à Rosny-sous-Bois, intervient rapidement avec un devis immédiat.")
    h += f'''<section><div class="wrap">
  <div class="deux"><div class="bloc"><h2>Votre vitrier de proximité {e(an)}</h2><p>{e(v["texte"])}</p><p>{e(v["detail"])}</p>
  <p>Nous intervenons aussi {"près d'ici" if v.get("parent") else "dans les villes voisines"} : {e(", ".join(v["voisines"]))}.</p></div>
  <div class="bloc"><h2>Nos interventions {e(an)}</h2><ul>
    <li>Urgence vitre cassée 24h/24 et mise en sécurité</li>
    <li>Remplacement de vitre, de vitrine et de double vitrage</li>
    <li>Miroirs sur mesure et crédences en verre</li>
    <li>Parois de douche et pare-baignoire</li>
    <li>Verres de verrière et de marquise</li>
    <li>Fenêtres, portes-fenêtres et volets roulants</li>
    <li>Réglage de fenêtres et remplacement de crémones</li>
  </ul><p><a href="/#services">Voir le détail de nos services →</a></p></div></div>
</div></section>
{bloc_avis()}
{bloc_faq(faq, f"Vitrier {an} : vos questions")}
{bloc_arrondissements(v) if v["slug"] == "vitrier-paris" or v.get("parent") else ""}
{"" if v.get("parent") else bloc_autres_villes(v, dep)}
'''
    h += pied()
    ecrire(chemin, h); PAGES.append((chemin, "0.8"))

# ---------------------------------------------------------------- réalisations
def page_realisations():
    chemin = "/realisations/"
    ld = [ENTREPRISE, fil_ld([("Accueil","/"),("Réalisations",chemin)])]
    h = tete("Réalisations avant / après | Miroiterie Winter, vitrier Rosny", "Photos avant / après de nos chantiers : vitre cassée, baie vitrée, porte-fenêtre, fenêtre PVC, miroir sur mesure. Miroiterie Winter, vitrier à Rosny-sous-Bois.", chemin, ld)
    h += '<div class="wrap">' + fil([("Accueil","/"),("Réalisations",chemin)]) + '</div>'
    h += hero("Nos chantiers", "Réalisations avant / après", "Quelques chantiers récents en Île-de-France. Suivez-nous sur Instagram pour voir les nouveaux.", facts=False)
    cartes = "".join(f'<figure class="real">{img(f, "Avant / après : " + t)}<figcaption><b>{e(t)}</b><span>{e(d)}</span></figcaption></figure>' for f,t,d in REALISATIONS)
    h += f'<section><div class="wrap"><div class="galerie">{cartes}</div><p><a class="lien-fort" href="{INSTAGRAM}" rel="noopener" target="_blank">Plus de réalisations sur Instagram →</a></p></div></section>'
    h += pied()
    ecrire(chemin, h); PAGES.append((chemin, "0.7"))

# ---------------------------------------------------------------- mentions légales
def page_mentions():
    chemin = "/mentions-legales/"
    h = tete("Mentions légales | Miroiterie Winter", "Mentions légales du site miroiterie-winter.fr.", chemin, robots="noindex,follow")
    h += '<div class="wrap">' + fil([("Accueil","/"),("Mentions légales",chemin)]) + '</div>'
    h += f'''<section><div class="wrap texte">
<h1>Mentions légales</h1>
<h2>Éditeur du site</h2>
<p>Miroiterie Winter, Dwinter Morisseau, entrepreneur individuel<br>{ADRESSE}<br>SIRET : 982 315 723 00014<br>Téléphone : {TEL} · E-mail : <a href="mailto:{MAIL}">{MAIL}</a><br>Directeur de la publication : Dwinter Morisseau</p>
<h2>Hébergement</h2>
<p>Netlify, Inc., San Francisco, Californie, États-Unis · www.netlify.com</p>
<h2>Données personnelles</h2>
<p>Ce site ne dépose pas de cookie publicitaire et ne contient pas de formulaire. Les informations que vous nous transmettez par téléphone, SMS ou e-mail servent uniquement à répondre à votre demande et à établir votre devis. Vous pouvez demander leur suppression à tout moment à {MAIL}.</p>
<h2>Propriété</h2>
<p>Les textes, photos et logos de ce site appartiennent à Miroiterie Winter. Toute reproduction sans autorisation est interdite.</p>
<p>Seul le site miroiterie-winter.fr est édité par Miroiterie Winter.</p>
</div></section>
'''
    h += pied()
    ecrire(chemin, h)

def page_404():
    h = tete("Page introuvable | Miroiterie Winter", "Cette page n'existe pas.", "/404/", robots="noindex")
    h += hero("Erreur 404", "Page introuvable", "Cette page n'existe pas ou a été déplacée. Pour une urgence, appelez-nous directement.", facts=False)
    h += '<section><div class="wrap"><p><a class="lien-fort" href="/">← Retour à l\'accueil</a></p></div></section>'
    h += pied()
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(h.replace(" ?", "\u00a0?"))

page_accueil()
for v in VILLES:
    if v["slug"] in VILLES_ACTIVES: page_ville(v)
for v in ARRONDISSEMENTS:
    page_ville(v)
for d in DEPARTEMENTS:
    page_departement(d)
page_mentions()
page_404()

sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAINE}{p}</loc><lastmod>{DATE}</lastmod><priority>{pr}</priority></url>\n" for p,pr in PAGES) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAINE}/sitemap.xml\n")
print(len(PAGES), "pages indexables")
