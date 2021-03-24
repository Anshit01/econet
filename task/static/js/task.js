$(document).ready(function () {
  $(".taskpostholder").click(function () {
    $("#post-modal")
      .children()
      .children()
      .html(
        '<img src="https://media3.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" />'
      );
    $("#post-modal").modal("show");
    post_id = $(this).attr("post-id");
    $.get("/getpost?id=" + post_id, function (data, status) {
      if (status && data != "Not Found") {
        $("#post-modal").children().children().html(data);
      } else {
        $("#post-modal").modal("hide");
      }
    });
  });
});
