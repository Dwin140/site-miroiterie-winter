# Départements d'Île-de-France et villes principales (demande de Dwinter le 23/11/2026 :
# « toutes les villes du 94, 93, 92, 91, 77, 95, 78 »).
# Choix : une page par département (avec la liste de ses communes) + une page pour les villes
# principales seulement. Des centaines de pages presque identiques seraient vues par Google
# comme des pages satellites et pénaliseraient tout le site.
# Chaque ville a son propre « texte » ; « theme » choisit un paragraphe et une question parmi THEMES.

DEPARTEMENTS = [
  dict(num="93", nom="Seine-Saint-Denis", slug="vitrier-seine-saint-denis-93", de="en Seine-Saint-Denis",
       texte="La Seine-Saint-Denis est notre département : notre base est à Rosny-sous-Bois. C'est là que nous intervenons le plus souvent, de jour comme de nuit.",
       autres=["Clichy-sous-Bois","Montfermeil","Sevran","Tremblay-en-France","Villepinte","Le Blanc-Mesnil","Le Bourget","La Courneuve","Saint-Ouen-sur-Seine","Épinay-sur-Seine","Stains","Pierrefitte-sur-Seine","Villetaneuse","L'Île-Saint-Denis","Dugny","Le Pré-Saint-Gervais","Les Pavillons-sous-Bois","Coubron","Vaujours","Gournay-sur-Marne"]),
  dict(num="94", nom="Val-de-Marne", slug="vitrier-val-de-marne-94", de="dans le Val-de-Marne",
       texte="Le Val-de-Marne commence juste au sud de Rosny-sous-Bois, avec Fontenay-sous-Bois et Vincennes. Nous y intervenons très souvent, des bords de Marne aux bords de Seine.",
       autres=["Bry-sur-Marne","Charenton-le-Pont","Saint-Maurice","Villejuif","Le Kremlin-Bicêtre","Cachan","L'Haÿ-les-Roses","Chevilly-Larue","Thiais","Choisy-le-Roi","Orly","Alfortville","Bonneuil-sur-Marne","Sucy-en-Brie","Villiers-sur-Marne","Le Plessis-Trévise","Chennevières-sur-Marne","Ormesson-sur-Marne","Villeneuve-Saint-Georges","Boissy-Saint-Léger"]),
  dict(num="92", nom="Hauts-de-Seine", slug="vitrier-hauts-de-seine-92", de="dans les Hauts-de-Seine",
       texte="Dans les Hauts-de-Seine, nous intervenons chez les particuliers comme dans les bureaux, de La Défense aux bords de Seine.",
       autres=["Levallois-Perret","Clichy","Asnières-sur-Seine","Gennevilliers","Rueil-Malmaison","Puteaux","Suresnes","Saint-Cloud","Sèvres","Meudon","Clamart","Vanves","Malakoff","Montrouge","Châtillon","Bagneux","Antony","Châtenay-Malabry","Le Plessis-Robinson","Garches"]),
  dict(num="91", nom="Essonne", slug="vitrier-essonne-91", de="en Essonne",
       texte="En Essonne, nous intervenons dans les maisons et les résidences, du nord du département jusqu'à Évry et Corbeil.",
       autres=["Athis-Mons","Juvisy-sur-Orge","Viry-Châtillon","Grigny","Ris-Orangis","Draveil","Yerres","Brunoy","Montgeron","Vigneux-sur-Seine","Sainte-Geneviève-des-Bois","Brétigny-sur-Orge","Longjumeau","Chilly-Mazarin","Les Ulis","Orsay","Gif-sur-Yvette","Étampes","Mennecy","Arpajon"]),
  dict(num="77", nom="Seine-et-Marne", slug="vitrier-seine-et-marne-77", de="en Seine-et-Marne",
       texte="La Seine-et-Marne commence à quelques kilomètres de Rosny-sous-Bois, après Gagny et Neuilly-sur-Marne. Nous y intervenons surtout dans l'ouest du département, de Chelles à Meaux et Melun.",
       autres=["Champs-sur-Marne","Noisiel","Lognes","Émerainville","Vaires-sur-Marne","Pontault-Combault","Roissy-en-Brie","Ozoir-la-Ferrière","Bussy-Saint-Georges","Serris","Chessy","Villeparisis","Mitry-Mory","Claye-Souilly","Dammartin-en-Goële","Savigny-le-Temple","Combs-la-Ville","Brie-Comte-Robert","Fontainebleau","Provins"]),
  dict(num="95", nom="Val-d'Oise", slug="vitrier-val-d-oise-95", de="dans le Val-d'Oise",
       texte="Dans le Val-d'Oise, nous intervenons d'Argenteuil à Cergy et dans la vallée de Montmorency, pour les urgences comme pour les projets.",
       autres=["Pontoise","Bezons","Ermont","Eaubonne","Franconville","Sannois","Saint-Gratien","Enghien-les-Bains","Deuil-la-Barre","Gonesse","Goussainville","Villiers-le-Bel","Taverny","Herblay-sur-Seine","Cormeilles-en-Parisis","Saint-Ouen-l'Aumône","Osny","Domont","Persan","L'Isle-Adam"]),
  dict(num="78", nom="Yvelines", slug="vitrier-yvelines-78", de="dans les Yvelines",
       texte="Dans les Yvelines, nous intervenons de Versailles à Saint-Germain-en-Laye et Saint-Quentin-en-Yvelines, dans les appartements anciens comme dans les maisons.",
       autres=["Le Chesnay-Rocquencourt","Vélizy-Villacoublay","Viroflay","Chatou","Le Vésinet","Croissy-sur-Seine","Houilles","Le Pecq","Maisons-Laffitte","Conflans-Sainte-Honorine","Les Mureaux","Mantes-la-Jolie","Plaisir","Trappes","Guyancourt","Élancourt","Rambouillet","Marly-le-Roi","Carrières-sur-Seine","Chambourcy"]),
]

# Départements des villes qui avaient déjà une page
DEP_EXISTANTES = {
  "vitrier-montreuil":"93","vitrier-noisy-le-sec":"93","vitrier-villemomble":"93","vitrier-bondy":"93","vitrier-bagnolet":"93",
  "vitrier-romainville":"93","vitrier-gagny":"93","vitrier-le-raincy":"93","vitrier-neuilly-plaisance":"93","vitrier-neuilly-sur-marne":"93",
  "vitrier-noisy-le-grand":"93","vitrier-fontenay-sous-bois":"94","vitrier-vincennes":"94","vitrier-le-perreux-sur-marne":"94",
  "vitrier-nogent-sur-marne":"94",
}

# Paragraphe + question par thème. {an} = « à Créteil », « au Raincy »…
THEMES = [
  ("Pour un commerce, nous mettons d'abord la vitrine en sécurité après une casse, puis nous posons le verre neuf.",
   ("Remplacez-vous les vitrines de commerce {an} ?","Oui. Nous sécurisons la vitrine cassée puis posons un verre neuf adapté, feuilleté si besoin.")),
  ("Quand la fenêtre est en bon état, nous remplaçons seulement le double vitrage : c'est plus simple et moins cher qu'une fenêtre neuve.",
   ("Peut-on changer seulement le double vitrage {an} ?","Oui. Si le cadre est en bon état, nous remplaçons uniquement le vitrage.")),
  ("Nous découpons les miroirs à vos mesures : ronds, ovales ou rectangulaires, pour une entrée, une chambre ou une salle de bain.",
   ("Faites-vous des miroirs sur mesure {an} ?","Oui : miroirs ronds, ovales ou rectangulaires, à vos mesures, fournis et posés chez vous.")),
  ("Pour une salle de bain, nous mesurons sur place et posons une paroi de douche ou un pare-baignoire adapté.",
   ("Posez-vous des parois de douche {an} ?","Oui : parois fixes ou coulissantes et pare-baignoire, mesurés chez vous puis posés.")),
  ("Dans la cuisine, nous posons des crédences en verre laqué, faciles à nettoyer, découpées à la mesure.",
   ("Posez-vous des crédences en verre {an} ?","Oui. Nous posons des crédences en verre laqué, découpées aux mesures de votre cuisine.")),
  ("Verrières, marquises et vérandas : nous changeons les verres abîmés en gardant la structure existante.",
   ("Remplacez-vous les verres de verrière ou de marquise {an} ?","Oui. Nous mesurons chaque verre et posons des verres neufs dans l'armature existante.")),
  ("Nous posons des volets roulants manuels, électriques ou solaires, sur des fenêtres neuves ou existantes.",
   ("Posez-vous des volets roulants {an} ?","Oui : manuels, électriques ou solaires, fournis et posés.")),
  ("Une fenêtre ou une porte-fenêtre qui ferme mal se règle souvent sans la changer, parfois avec une crémone neuve.",
   ("Réglez-vous les fenêtres qui ferment mal {an} ?","Oui. Un réglage ou une crémone neuve suffit souvent, sans changer la fenêtre.")),
  ("Pour les portes vitrées, nous posons du verre clair, dépoli ou cathédrale, coupé à la mesure.",
   ("Remplacez-vous le verre d'une porte vitrée {an} ?","Oui : verre clair, dépoli ou cathédrale, coupé à la mesure et posé dans votre porte.")),
  ("Nous travaillons aussi pour les syndics, les agences et les bailleurs, dans les logements comme dans les parties communes.",
   ("Travaillez-vous pour les copropriétés {an} ?","Oui. Nous intervenons pour les syndics, les agences et les bailleurs, sur les logements et les parties communes.")),
]

def V(slug, nom, cp, dep, voisines, texte, theme, a=None):
    d = dict(slug=slug, nom=nom, cp=cp, dep=dep, voisines=voisines, texte=texte, theme=theme)
    if a: d["a"] = a
    return d

NOUVELLES_VILLES = [
  # 93
  V("vitrier-saint-denis","Saint-Denis","93200","93",["Saint-Ouen-sur-Seine","Aubervilliers","Épinay-sur-Seine"],"Saint-Denis mêle centre ancien autour de la basilique, quartiers récents près du Stade de France et nombreux commerces.",0),
  V("vitrier-aubervilliers","Aubervilliers","93300","93",["Pantin","Saint-Denis","La Courneuve"],"Aubervilliers, le long du canal Saint-Denis, compte beaucoup d'ateliers, de commerces et d'immeubles d'habitation.",9),
  V("vitrier-pantin","Pantin","93500","93",["Les Lilas","Aubervilliers","Bobigny","Paris 19e"],"Pantin, au bord du canal de l'Ourcq, a beaucoup d'anciens bâtiments industriels transformés en lofts et en bureaux, souvent très vitrés.",5),
  V("vitrier-aulnay-sous-bois","Aulnay-sous-Bois","93600","93",["Sevran","Le Blanc-Mesnil","Livry-Gargan"],"Aulnay-sous-Bois est une grande ville avec de nombreux quartiers pavillonnaires et des résidences.",6),
  V("vitrier-drancy","Drancy","93700","93",["Bobigny","Le Bourget","Le Blanc-Mesnil"],"À Drancy, ville résidentielle entre pavillons et immeubles, nous remplaçons vitres et doubles vitrages.",1),
  V("vitrier-les-lilas","Les Lilas","93260","93",["Romainville","Bagnolet","Le Pré-Saint-Gervais","Paris 19e et 20e"],"Les Lilas, petite ville voisine de Romainville et de Paris, compte des maisons et des immeubles anciens.",8),
  V("vitrier-livry-gargan","Livry-Gargan","93190","93",["Les Pavillons-sous-Bois","Le Raincy","Sevran","Clichy-sous-Bois"],"Livry-Gargan est une ville surtout pavillonnaire, au nord du Raincy et de Villemomble.",7),
  V("vitrier-bobigny","Bobigny","93000","93",["Drancy","Pantin","Noisy-le-Sec","Bondy"],"Bobigny, préfecture de la Seine-Saint-Denis, est tout près de Noisy-le-Sec et de Rosny-sous-Bois.",9),
  # 94
  V("vitrier-creteil","Créteil","94000","94",["Maisons-Alfort","Saint-Maur-des-Fossés","Bonneuil-sur-Marne"],"Créteil, préfecture du Val-de-Marne, mêle résidences autour du lac, immeubles et maisons dans le vieux Créteil.",3),
  V("vitrier-vitry-sur-seine","Vitry-sur-Seine","94400","94",["Ivry-sur-Seine","Villejuif","Choisy-le-Roi"],"Vitry-sur-Seine, au bord de la Seine, compte autant de pavillons que de grands immeubles.",1),
  V("vitrier-champigny-sur-marne","Champigny-sur-Marne","94500","94",["Saint-Maur-des-Fossés","Le Perreux-sur-Marne","Villiers-sur-Marne"],"Champigny-sur-Marne, sur les bords de Marne, compte de nombreux pavillons.",6),
  V("vitrier-saint-maur-des-fosses","Saint-Maur-des-Fossés","94100","94",["Joinville-le-Pont","Champigny-sur-Marne","Créteil"],"Saint-Maur-des-Fossés, dans la boucle de la Marne, compte beaucoup de maisons anciennes et de villas.",5),
  V("vitrier-ivry-sur-seine","Ivry-sur-Seine","94200","94",["Vitry-sur-Seine","Charenton-le-Pont","Paris 13e"],"Ivry-sur-Seine, aux portes de Paris, a de nombreux anciens ateliers devenus logements et bureaux.",2),
  V("vitrier-maisons-alfort","Maisons-Alfort","94700","94",["Charenton-le-Pont","Créteil","Alfortville"],"Maisons-Alfort, entre Seine et Marne, compte immeubles et maisons, et nous y posons souvent miroirs et crédences.",4),
  V("vitrier-saint-mande","Saint-Mandé","94160","94",["Vincennes","Paris 12e","Paris 20e"],"Saint-Mandé, entre Vincennes et le 12e arrondissement, a beaucoup d'immeubles anciens aux grandes fenêtres.",8),
  V("vitrier-joinville-le-pont","Joinville-le-Pont","94340","94",["Saint-Maur-des-Fossés","Nogent-sur-Marne","Champigny-sur-Marne"],"Joinville-le-Pont, sur les bords de Marne, mêle maisons et résidences.",7),
  # 92
  V("vitrier-boulogne-billancourt","Boulogne-Billancourt","92100","92",["Issy-les-Moulineaux","Saint-Cloud","Paris 16e"],"Boulogne-Billancourt, très peuplée, compte beaucoup d'appartements où nous posons miroirs, crédences et parois de douche.",2),
  V("vitrier-nanterre","Nanterre","92000","92",["Rueil-Malmaison","Colombes","Puteaux"],"Nanterre, préfecture des Hauts-de-Seine, mêle quartiers d'affaires, résidences et maisons.",9),
  V("vitrier-courbevoie","Courbevoie","92400","92",["Puteaux","La Garenne-Colombes","Levallois-Perret"],"Courbevoie, au pied des tours de La Défense, compte de nombreux bureaux et immeubles.",0),
  V("vitrier-colombes","Colombes","92700","92",["Asnières-sur-Seine","Nanterre","Bois-Colombes"],"Colombes mêle pavillons et immeubles, avec beaucoup de fenêtres et de volets à entretenir.",6),
  V("vitrier-neuilly-sur-seine","Neuilly-sur-Seine","92200","92",["Levallois-Perret","Courbevoie","Paris 16e et 17e"],"À Neuilly-sur-Seine, beaucoup d'hôtels particuliers et de grands appartements ont des miroirs muraux et des portes vitrées.",8),
  V("vitrier-issy-les-moulineaux","Issy-les-Moulineaux","92130","92",["Boulogne-Billancourt","Vanves","Paris 15e"],"Issy-les-Moulineaux, au bord de la Seine, compte beaucoup de bureaux et d'immeubles récents.",3),
  # 91
  V("vitrier-evry-courcouronnes","Évry-Courcouronnes","91000","91",["Corbeil-Essonnes","Ris-Orangis","Lisses"],"Évry-Courcouronnes, préfecture de l'Essonne, compte résidences, maisons et commerces.",0,a="à Évry-Courcouronnes"),
  V("vitrier-massy","Massy","91300","91",["Palaiseau","Antony","Chilly-Mazarin"],"Massy, autour de sa gare, compte beaucoup de quartiers récents et de résidences.",1),
  V("vitrier-palaiseau","Palaiseau","91120","91",["Massy","Orsay","Saclay"],"Palaiseau, au pied du plateau de Saclay, mêle maisons anciennes et logements récents.",7),
  V("vitrier-corbeil-essonnes","Corbeil-Essonnes","91100","91",["Évry-Courcouronnes","Saint-Germain-lès-Corbeil","Mennecy"],"Corbeil-Essonnes, au confluent de la Seine et de l'Essonne, a un centre ancien et de nombreuses maisons.",5),
  V("vitrier-savigny-sur-orge","Savigny-sur-Orge","91600","91",["Juvisy-sur-Orge","Viry-Châtillon","Morsang-sur-Orge"],"Savigny-sur-Orge, dans la vallée de l'Orge, est une ville surtout pavillonnaire.",6),
  # 77
  V("vitrier-chelles","Chelles","77500","77",["Gagny","Neuilly-sur-Marne","Vaires-sur-Marne"],"Chelles, sur les bords de Marne, est la ville de Seine-et-Marne la plus proche de Rosny-sous-Bois.",7),
  V("vitrier-meaux","Meaux","77100","77",["Trilport","Nanteuil-lès-Meaux","Villenoy"],"Meaux, autour de sa cathédrale et de son centre ancien, compte de nombreuses maisons anciennes.",8),
  V("vitrier-melun","Melun","77000","77",["Dammarie-les-Lys","Le Mée-sur-Seine","Vaux-le-Pénil"],"Melun, préfecture de la Seine-et-Marne, s'étend autour de l'île Saint-Étienne, sur la Seine.",9),
  V("vitrier-torcy","Torcy","77200","77",["Noisiel","Lognes","Champs-sur-Marne"],"Torcy, près de la base de loisirs de Vaires-Torcy, compte maisons et résidences récentes.",3),
  V("vitrier-lagny-sur-marne","Lagny-sur-Marne","77400","77",["Thorigny-sur-Marne","Saint-Thibault-des-Vignes","Bussy-Saint-Georges"],"Lagny-sur-Marne a un centre ancien au bord de la Marne, avec beaucoup de fenêtres et de portes vitrées anciennes.",5),
  # 95
  V("vitrier-argenteuil","Argenteuil","95100","95",["Bezons","Sannois","Colombes"],"Argenteuil, la ville la plus peuplée du Val-d'Oise, mêle pavillons, immeubles et commerces au bord de la Seine.",0),
  V("vitrier-cergy","Cergy","95000","95",["Pontoise","Osny","Vauréal"],"Cergy, au cœur de Cergy-Pontoise, compte beaucoup de résidences et de maisons récentes.",3),
  V("vitrier-sarcelles","Sarcelles","95200","95",["Garges-lès-Gonesse","Villiers-le-Bel","Saint-Brice-sous-Forêt"],"Sarcelles mêle grands ensembles et quartiers pavillonnaires.",9),
  V("vitrier-garges-les-gonesse","Garges-lès-Gonesse","95140","95",["Sarcelles","Gonesse","Stains"],"Garges-lès-Gonesse, voisine de Sarcelles, compte de nombreuses résidences et maisons.",1),
  V("vitrier-montmorency","Montmorency","95160","95",["Enghien-les-Bains","Soisy-sous-Montmorency","Deuil-la-Barre"],"Montmorency, sur les coteaux près de sa forêt, compte beaucoup de maisons anciennes.",5),
  # 78
  V("vitrier-versailles","Versailles","78000","78",["Le Chesnay-Rocquencourt","Viroflay","Saint-Cyr-l'École"],"À Versailles, beaucoup d'appartements anciens et d'hôtels particuliers ont de grandes fenêtres, des miroirs et des portes vitrées.",2),
  V("vitrier-saint-germain-en-laye","Saint-Germain-en-Laye","78100","78",["Le Pecq","Chambourcy","Poissy"],"Saint-Germain-en-Laye, autour de son château et de son centre ancien, compte beaucoup d'immeubles et de maisons anciennes.",8),
  V("vitrier-poissy","Poissy","78300","78",["Saint-Germain-en-Laye","Carrières-sous-Poissy","Villennes-sur-Seine"],"Poissy, au bord de la Seine, mêle centre ancien, pavillons et résidences.",6),
  V("vitrier-sartrouville","Sartrouville","78500","78",["Houilles","Maisons-Laffitte","Montesson"],"Sartrouville, dans la boucle de la Seine, est une ville surtout pavillonnaire.",7),
  V("vitrier-montigny-le-bretonneux","Montigny-le-Bretonneux","78180","78",["Guyancourt","Voisins-le-Bretonneux","Trappes"],"Montigny-le-Bretonneux, au cœur de Saint-Quentin-en-Yvelines, compte beaucoup de maisons et de résidences récentes.",4),
]
