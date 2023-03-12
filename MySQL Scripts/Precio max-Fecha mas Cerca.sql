select distinct p1.Codigo,p1.Suplidor, p1.Fecha, p1.Precio_sin_Itbis, p1.Itbis, p1.Precio_con_Itbis, p1.Marca from precios as p1 
join (select Codigo, min(abs(datediff(Fecha,Now()))) as dif from precios group by Codigo) as p2
on p1.Codigo = p2.Codigo and abs(datediff(p1.Fecha,Now())) = p2.dif
join (select Codigo, max(Precio_sin_Itbis) as Precio_sin_Itbis from precios group by Codigo) as p3
on p1.Codigo = p3.Codigo and p1.Precio_sin_Itbis = p3.Precio_sin_Itbis
order by p1.Codigo


