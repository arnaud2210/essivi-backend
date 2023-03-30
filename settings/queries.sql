-- POSTGRESQL VIEWS REQUESTS


-- Vue affichant le reste en stock, le montant d'une commande par date

/*select "idCustomer", "firstnameOfCustomer", "labelOfProduct", "unitPrice", "productQuantity", "ordered_quantity", ("unitPrice" * "ordere
d_quantity") as "total", ("productQuantity" - "ordered_quantity") as "stock_quantity", "ordered_date"  from customers c, orders o, products p wher
e p."idProduct" = o."product_id" and c."idCustomer" = o."customer_id" order by "ordered_date";*/


-- vue affichant le montant total par commande et par date d'un client 

create or replace view "totalOrderLine" 
as 
select "idCustomer", "firstnameOfCustomer", "labelOfProduct", "unitPrice", "ordered_quantity", ("unitPrice" * "ordered_quantity") as "total", "ordered_date"  
from customers c, orders o, products p 
where p."idProduct" = o."product_id" and c."idCustomer" = o."customer_id" order by "ordered_date";


-- Vue affichant le total d'une commande par date et par client à une date donnée

create or replace view "totalInvoice" 
as 
select "idCustomer", "firstnameOfCustomer", sum("ordered_quantity") as "items", sum("total") as
 "TotalFacture", extract(year from "ordered_date") as "DateFacture" 
 from "totalOrderLine" 
 group by "firstnameOfCustomer", "idCustomer", extract(year from "ordered_date");

-- Vue affichant la quantité restante en stock après commande
-- 03/02/2023

create or replace view "stock_quantity" 
as 
select "idProduct", "labelOfProduct", "productQuantity", "ordered_quantity" 
from products p, orders o 
where p."idProduct" = o."product_id" group by p."idProduct", "ordered_quantity";


-- Vue affichant le nombre de livraisons par jour

create view "deliverPerDay" as select date_part('day', "delivery_date") as "Jour", count(*) as "nombre de livraisons" from delivers grou
p by "delivery_date";


-- Vue affichant le chiffre d'affaire par jour

create view "chiffre_jour" as select date_part('day', "delivery_date"), sum("amount_collected") as "chiffre_jour" from delivers group by
 date_part('day', "delivery_date") order by 1 asc;


-- Vue affichant le chiffre d'affaire par mois

create view "chiffre_mois" as select date_part('month', "delivery_date"), sum("amount_collected") as "chiffre_mois" from delivers group
by date_part('month', "delivery_date") order by 1 asc;


-- 30/01/2023

-- NOMBRE DE PRODUITS PAR CATEGORIE

create view "quantiteParCategorie" as 
select c.id, "labelOfCat" as "catégorie", count("category_id") as "quantité" 
from categories c join products p 
on c.id = p."category_id" 
group by "category_id", "labelOfCat", c.id;


-- PRIX PAR COMMANDE --

create view "prixParCommande" as 
select o."product_id", "labelOfProduct", p."unitPrice", sum("ordered_quantity") as "items", ("unitPrice"*"ordered_quantity") as "prix_reel", p."category_id", extract(month from o."ordered_date") as "date_part"
from products p join orders o 
on p."idProduct" = o."product_id" 
group by "product_id", p."unitPrice", o."ordered_quantity", "labelOfProduct", p."category_id", o."ordered_date";


-- CHIFFRE D'AFFAIRE PAR CATEGORIE GROUPE PAR MOIS

create or replace view "chiffreCatPerMonth" as 
select "labelOfCat", sum("prix_reel") as "chiffre_per_month", to_char(to_date("date_part"::text, 'MM'), 'Month') as "Mois" 
from categories c join "prixParCommande" p 
on c.id = p."category_id" 
group by "labelOfCat", "date_part"
order by 1,2 asc;

to_date("Mois"::text, 'MM'), 'Month'), "chiffre_affaire"


-- CHIFFRE D'AFFAIRE PAR MOIS

create or replace view "chiffrePerMonth" as
select to_char(to_date("Mois"::text, 'MM'), 'Month'), sum("chiffre_per_month") as "chiffre_affaire" 
from "chiffreCatPerMonth" group by "Mois"; --order by 1,2 asc;


-- NOMBRE DE CLIENTS PAR AGENTS

create view "nombreClientParAgent" as 
select u."firstname" || ' ' || u."lastname" as "Agent", count(c."user_id") as "nombre_client" 
from customers c join users u 
on u."idUser" = c."user_id"
group by c."user_id", u."firstname", u."lastname";


-- NOMBRE DE PERSONNEL PAR TYPE

create view "typePersonnel" as 
select label, count("role_id") as "nombreAgent" 
from users u join roles r 
on r.id = u."role_id"
group by r.id, label;


-- 03/02/2023

CREATE OR REPLACE FUNCTION stock_operation()
  RETURNS TRIGGER
  AS
$$
DECLARE
	qteprod integer;
	qtecom integer;
	restant integer;
BEGIN
	select "productQuantity" into qteprod 
	from products where "idProduct" = new."product_id";
	qtecom := new.ordered_quantity;
	RAISE NOTICE 'value : %', qteprod;
	RAISE NOTICE 'value : %', qtecom;
	
	if qtecom <= qteprod and qtecom > 0 then
		RAISE NOTICE 'value : %', qtecom;
		restant := qteprod - qtecom;
		RAISE NOTICE 'value : %', restant;
		update products set "productQuantity" = restant
		where "idProduct" = new."product_id";
	else
		RAISE EXCEPTION 'Insertion impossible';
	end if;
	return new;
END;
$$ LANGUAGE PLPGSQL


CREATE TRIGGER update_product
  AFTER INSERT
  ON orders
  FOR EACH ROW
  EXECUTE PROCEDURE stock_operation();


-- 07/02/2023

-- VUE AFFICHANT LES COMMANDES NON LIVREES

create view "ordersNotDelivered" 
as 
select * from orders 
where "idOrdered" not in (select d."ordered_id" from orders o join delivers d o
n o."idOrdered" = d."ordered_id");
