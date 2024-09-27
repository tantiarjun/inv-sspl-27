{
  /* <script> */
}
// Generate a unique invoice number
function generateInvoiceNumber() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const seconds = String(now.getSeconds()).padStart(2, "0");
  return `INV-${year}${month}${day}${hours}${minutes}${seconds}`;
}

// Set the generated invoice number on page load
window.onload = function () {
  document.getElementById("invoice").value = generateInvoiceNumber();
};

let itemCount = 0;
let items = [];

// Fetch item rate via AJAX
function fetchRate() {
  const item_id = $("#item_name").val();
  if (item_id) {
    $.get("/get-item-rate/", { item_name_id: item_id }, function (data) {
      $("#rate").val(data.rate);
      calculateTotal();
    });
  } else {
    $("#rate").val("");
    $("#total").val("");
  }
}

// Calculate total amount based on rate and quantity
function calculateTotal() {
  const rate = parseFloat($("#rate").val()) || 0;
  const quantity = parseInt($("#quantity").val()) || 0;
  if (quantity < 0) {
    quantity *= -1;
  }
  const total = rate * quantity;
  $("#total").val(total.toFixed(2));
}

// Add item to the table and hidden input for form submission
function addItem() {
  const item_id = $("#item_name").val();
  const item_name = $("#item_name option:selected").text();
  const rate = $("#rate").val();
  const quantity = $("#quantity").val();
  const total = $("#total").val();

  if (item_id && rate && quantity && total) {
    itemCount++;

    // Append item to the table
    const row = `<tr>
                <td>${itemCount}</td>
                <td>${item_name}</td>
                <td>${rate}</td>
                <td>${quantity}</td>
                <td>${total}</td>
                <td><button type="button" onclick="removeItem(this, ${
                  itemCount - 1
                })">Delete</button></td>
            </tr>`;
    $("#itemTable tbody").append(row);

    // Append hidden input for form submission
    $("form").append(
      `<input type="hidden" name="items[]" value="${item_id},${quantity},${total}" id="item_${itemCount}">`
    );

    // Clear the input fields
    $("#item_name").val("");
    $("#rate").val("");
    $("#quantity").val("");
    $("#total").val("");
  } else {
    alert("Please fill out all the fields for the item.");
  }
}

// Remove item from the table and hidden input
function removeItem(button, index) {
  $(button).closest("tr").remove();
  $(`#item_${index + 1}`).remove();
}

// Validate if any items are added before submitting the form
function validateItems(event) {
  const itemCount = $("#itemTable tbody tr").length;
  if (itemCount === 0) {
    event.preventDefault(); // Prevent form submission
    alert("Please add at least one item before submitting.");
  }
}
// </script>
