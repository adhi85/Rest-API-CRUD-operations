send_request();
function send_request(param) {
  $.ajax({
    method: "GET",
    url: "api/book-list?" + param,
    success: function (result) {
      update(result);
    },
    error: function () {
      console.log("Error");
    },
  });
}

function update(data) {
  let row;
  let all_rows = "";

  Object.keys(data).forEach((key) => {
    element = data[key];
    row =
      "<tr><td>" +
      element["name"] +
      "</td>" +
      "<td>" +
      element["author"] +
      "</td>" +
      "<td>" +
      element["category"] +
      "</td>" +
      "</tr>";
    all_rows = all_rows + row;
  });

  $("#myTable tbody").html(all_rows);
}

function find_author() {
  let author = document.getElementById("author").value;
  let param = "author=" + author;
  send_request(param);
}

function book_type(category) {
  document.getElementById("author").value = "";
  let param = "category=" + category;
  send_request(param);
}
