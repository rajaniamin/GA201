db.createCollection("Restaurants", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "address", "phone_number", "cuisine", "rating"],
         properties: {
            id: {
               bsonType: "int"
            },
            name: {
               bsonType: "string"
            },
            address: {
               bsonType: "string"
            },
            phone_number: {
               bsonType: "string"
            },
            cuisine: {
               bsonType: "string"
            },
            rating: {
               bsonType: "decimal",
               minimum: 0,
               maximum: 999.99
            }
         }
      }
   }
})
-------------------------------------------------------------------------------------

db.Restaurants.insertMany([
   {
      name: 'Restaurant A',
      address: '123 Main Street',
      phone_number: '555-1234',
      cuisine: 'Italian',
      rating: 4.5
   },
   {
      name: 'Restaurant B',
      address: '456 Elm Avenue',
      phone_number: '555-5678',
      cuisine: 'Mexican',
      rating: 3.8
   },
   {
      name: 'Restaurant C',
      address: '789 Oak Road',
      phone_number: '555-9012',
      cuisine: 'Chinese',
      rating: 4.2
   },
   {
      name: 'Restaurant D',
      address: '321 Pine Lane',
      phone_number: '555-3456',
      cuisine: 'Indian',
      rating: 4.0
   },
   {
      name: 'Restaurant E',
      address: '654 Cedar Court',
      phone_number: '555-7890',
      cuisine: 'American',
      rating: 4.6
   }
])
------------------------------------------------------------------------------------------

db.Restaurants.find().sort({ rating: -1 })
--------------------------------------------------------------------------------------------

db.Restaurants.find({ $and: [ { delivery_available: true }, { rating: { $gt: 4 } } ] })
-------------------------------------------------------------------------------------------
db.Restaurants.find({ $or: [ { cuisine_type: null }, { cuisine_type: '' } ] })
------------------------------------------------------------------------------------------

db.Restaurants.countDocuments({ delivery_available: true })
------------------------------------------------------------------------------------------
db.Restaurants.find({ location: { $regex: 'New York' } })
------------------------------------------------------------------------------------------

db.Restaurants.find().sort({ rating: -1 }).limit(5)
------------------------------------------------------------------------------------------
db.Restaurants.deleteOne({ id: 3 })
--------------------------------------------------------------------------------------
