SELECT *

FROM item_pedido AS t1

LEFT JOIN pedido AS t2
ON t1.idPedido = t2.idPedido

WHERE t1.descTipoItem = 'bebida'
AND t1.descItem = '{desc_item}'
AND descUF = '{uf}'