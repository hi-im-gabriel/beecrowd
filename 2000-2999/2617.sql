select products.name, providers.name
from products, providers where
products.id_providers = providers.id
and providers.name = 'Ajax SA';
