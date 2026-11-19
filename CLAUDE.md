# Site de la Miroiterie Winter

Site vitrine pour la Miroiterie Winter, vitrier, miroitier et serrurier à Rosny-sous-Bois (93), qui intervient dans toute l'Île-de-France.
Le site est publié automatiquement par Netlify à chaque mise à jour de la branche `main`.

## Qui demande les changements
Dwinter Morisseau, le gérant. Il écrit en français, souvent en dictée depuis son iPhone (la transcription peut être approximative : deviner le sens le plus probable et le dire).
Il n'est pas développeur : réponses courtes, simples, sans jargon. Toujours finir par le lien pour voir le résultat.

## Façon de travailler
1. Faire le changement demandé sur une nouvelle branche et ouvrir une pull request.
2. Donner le lien de l'aperçu Netlify (« Deploy Preview ») pour qu'il regarde sur son téléphone.
3. Il valide → fusionner la pull request dans `main` (le site en ligne se met à jour en 1 minute).
   S'il dit « publie directement », on peut pousser sur `main` sans pull request.
4. Toujours vérifier le rendu sur téléphone (390 px de large) et sur ordinateur avant de proposer.

## Coordonnées à afficher (et rien d'autre)
- Téléphone : 07 83 38 68 24 (lien `tel:+33783386824`)
- E-mail : miroiterie.winter@gmail.com
- Adresse : 141 rue du Général Leclerc, 93110 Rosny-sous-Bois (jamais l'étage, l'escalier ni l'appartement)
- Note Google : 4,9 ★, 57 avis (au 19/11/2026). Dwinter a choisi une mise à jour chaque semaine : lire la fiche Google (Windsor.ai), proposer le changement en pull request et lui donner le lien d aperçu.

## Interdits
- Ne JAMAIS mettre d'IBAN, de coordonnées bancaires, de SIRET privé ou de prix de chantier sur le site.
- Ne jamais mettre le nom complet d'un client ni le prix d'un chantier sur une photo ou un avis (prénom seulement).
- Ne jamais dire que la fourniture vient d'un magasin.
- Accroche validée : « Devis immédiat » (jamais « devis gratuit »).
- Ne pas promettre ce qu'il n'a pas confirmé (ex. délais, garanties) : demander avant.

## Design system
- Couleurs : bleu marine `#16325f` (bandeau, titres), orange `#e8601c` (boutons d'appel, petites étiquettes, étoiles, bloc urgence), fond crème `#faf8f4`, blanc `#ffffff` pour les cartes, texte `#1d232c`, texte secondaire `#5b6472`, traits `#e3ded5`. Mode sombre déjà prévu dans les variables CSS de `index.html`.
- Polices : Archivo (titres, gras 700-800, souvent en MAJUSCULES) et Public Sans (texte). Sur les flyers imprimés, l'équivalent est Anton + Barlow.
- Logo : `images/logo-entete.png` (en-tête), `images/icone-512.png` et favicons (trois fenêtres avec triangles orange, « MIROITERIE WINTER / VITRIER SERRURIER »).
- Structure de la page : en-tête blanc (logo + téléphone) → bandeau bleu (accroche « Vitre cassée ? On intervient 24h/24. », bouton orange « Appeler maintenant », chiffres clés) → grille des services (la case « Urgence vitre cassée » en orange) → avant / après → avis Google + zone d'intervention → bandeau orange de contact → pied de page.
- Le numéro de téléphone doit toujours être visible et cliquable : le but n°1 du site est de faire appeler.
- Visuels avant / après : format 1080 x 1350, logo en haut, bande bleue « AVANT / APRÈS », photo avant à gauche (bordure bleue), photo après à droite (bordure orange), légende, pied orange avec le téléphone.
- Style d'écriture : phrases courtes, concrètes, vouvoiement, pas de superlatifs creux.

## Technique
- Site statique sans framework. Une page d'accueil unique (choix de Dwinter le 19/11/2026 : pas de pages services, villes ni réalisations) + mentions légales + 404. Ces pages HTML, `sitemap.xml` et `robots.txt` sont GÉNÉRÉES par `outils/generer_site.py` (textes, 8 services, FAQ, avis, zone, liens réseaux sont dans ce script ; les listes SERVICES et VILLES et leurs fonctions de page ne sont plus utilisées, gardées si on rouvre des pages plus tard).
- Pour modifier un texte, une ville, un service, les avis ou la note : changer `outils/generer_site.py`, puis lancer `python3 outils/generer_site.py .` à la racine. Ne pas modifier les .html à la main (ils seraient écrasés).
- Style commun : `style.css`. Animations : `site.js`. Images : `images/` (JPG/WebP < 300 Ko, texte `alt` en français).
- Domaine officiel : https://miroiterie-winter.fr (balises canonical, sitemap, données structurées). Réseaux : Instagram https://www.instagram.com/miroiterie_winter/ et fiche Google Maps.
- Référencement local : titre et description optimisés, données schema.org (entreprise, FAQ), sitemap, note Google à jour. Ordre de la page : bandeau, 8 services, avant/après, « Pourquoi nous appeler », note + avis + boutons Google Maps et Instagram + zone, FAQ, contact.
- Le site miroiteriewinter.fr (sans tiret, fait par Local.fr) n'est PAS le nôtre : ne jamais le copier mot pour mot.
- Vérifier chaque page sur téléphone (390 px) et ordinateur avant de proposer.
