function resetForm() {
  document.getElementById('createEmailForm').reset();
}

$(document).ready(function () {
  var dataTable = $("#email-table").DataTable({
    paging: true,
    searching: true,
    ordering: true,
    order: [[3, "desc"]],
    lengthChange: false,
    responsive: true,
    language: {
      info: "Displaying _START_ to _END_ of _TOTAL_ entries",
    },
  });

  function adjustPageLength() {
    var containerWidth = $(".hero-body").width();
    var pageLength = 10;

    if (containerWidth < 768) {
      pageLength = 3;
    } else if (containerWidth < 992) {
      pageLength = 5;
    } else {
      pageLength = 10;
    }

    dataTable.page.len(pageLength).draw();
  }

  adjustPageLength();
  var emailFilter = $("#email-table_filter").css("padding", "1.25rem");
  $(window).on("resize", adjustPageLength);
});
