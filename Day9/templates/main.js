// JavaScript code for form validation or any additional functionality

// Example: Form validation for adding a new dish
document.getElementById('addDishForm').addEventListener('submit', function(event) {
    var dishName = document.getElementById('dishName').value;
    var price = document.getElementById('price').value;
    var availability = document.getElementById('availability').value;

    if (!dishName || !price || !availability) {
        event.preventDefault();
        alert('Please fill in all the fields');
    }
});
