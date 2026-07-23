select packages.year, u1.name as sender, u2.name as receiver
from packages join
     users u1
     on packages.id_user_sender = u1.id join
     users u2
     on packages.id_user_receiver = u2.id
where (packages.year = 2015 or packages.color like 'blue')
     AND u2.address <> 'Taiwan' order by packages.year desc;
