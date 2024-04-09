Sample curl Request for Product Microservice
 
Add Product
 
curl --location 'http://172.27.67.20:30806/product' \
--header 'Content-Type: application/json' \
--data '{
    "cost": 5000,
    "id": 124,
    "name": "shoes"
}'
 
Get Product Details
 
curl --location 'http://172.27.65.68:30806/product/2e61bcb3-cd20-4766-a654-2ef33744aea5'