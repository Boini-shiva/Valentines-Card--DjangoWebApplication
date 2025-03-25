document.addEventListener('DOMContentLoaded', () => {
    const editBtns = document.querySelectorAll('#edit-btn');
    const deleteBtns = document.querySelectorAll('#delete-btn');
    
    // Example: handle button click event
    deleteBtns.forEach(button => {
        button.addEventListener('click', function (e) {
            if (!confirm("Are you sure you want to delete this card?")) {
                e.preventDefault();
            }
        });
    });
});

