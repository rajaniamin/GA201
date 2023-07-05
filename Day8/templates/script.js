// Function to open the modal
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = "block";
}

// Function to close the modal
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = "none";
}

// Function to pre-fill the edit dish form with existing data
function prefillEditDishForm(dishId) {
    const dish = dishes.find(d => d.id === dishId);
    if (dish) {
        const editDishForm = document.getElementById("edit-dish-form");
        const editDishIdField = document.getElementById("edit-dish-id");
        const editDishNameField = document.getElementById("edit-dish-name");
        const editDishPriceField = document.getElementById("edit-dish-price");
        const editDishAvailabilityField = document.getElementById("edit-dish-availability");
        
        editDishIdField.value = dish.id;
        editDishNameField.value = dish.name;
        editDishPriceField.value = dish.price;
        editDishAvailabilityField.checked = dish.availability;
        
        openModal("edit-dish-modal");
    }
}

// Function to pre-fill the delete dish form with existing data
function prefillDeleteDishForm(dishId) {
    const dish = dishes.find(d => d.id === dishId);
    if (dish) {
        const deleteDishForm = document.getElementById("delete-dish-form");
        const deleteDishIdField = document.getElementById("delete-dish-id");

        deleteDishIdField.value = dish.id;

        openModal("delete-dish-modal");
    }
}

// Function to pre-fill the update order form with existing data
function prefillUpdateOrderForm(orderId) {
    const order = orders.find(o => o.id === orderId);
    if (order) {
        const updateOrderForm = document.getElementById("update-order-form");
        const updateOrderIdField = document.getElementById("update-order-id");
        const updateStatusField = document.getElementById("update-status");

        updateOrderIdField.value = order.id;
        updateStatusField.value = order.status;

        openModal("update-order-modal");
    }
}

// Add event listeners to the buttons
document.addEventListener('DOMContentLoaded', function() {
    // Event listener for the "Add Dish" button
    const addDishBtn = document.getElementById("add-dish-btn");
    addDishBtn.addEventListener('click', function() {
        openModal("add-dish-modal");
    });

    // Event listener for the "Take Order" button
    const takeOrderBtn = document.getElementById("take-order-btn");
    takeOrderBtn.addEventListener('click', function() {
        openModal("take-order-modal");
    });

    // Event listener for the "Edit" buttons
    const editButtons = document.getElementsByClassName("edit-btn");
    Array.from(editButtons).forEach(function(button) {
        button.addEventListener('click', function() {
            const dishId = parseInt(button.getAttribute("data-id"));
            prefillEditDishForm(dishId);
        });
    });

    // Event listener for the "Delete" buttons
    const deleteButtons = document.getElementsByClassName("delete-btn");
    Array.from(deleteButtons).forEach(function(button) {
        button.addEventListener('click', function() {
            const dishId = parseInt(button.getAttribute("data-id"));
            prefillDeleteDishForm(dishId);
        });
    });

    // Event listener for the "Update Status" buttons
    const updateButtons = document.getElementsByClassName("update-btn");
    Array.from(updateButtons).forEach(function(button) {
        button.addEventListener('click', function() {
            const orderId = parseInt(button.getAttribute("data-id"));
            prefillUpdateOrderForm(orderId);
        });
    });

    // Event listener for the modal close buttons
    const closeButtons = document.getElementsByClassName("close");
    Array.from(closeButtons).forEach(function(button) {
        button.addEventListener('click', function() {
            const modalId = button.parentElement.parentElement.id;
            closeModal(modalId);
        });
    });
});
