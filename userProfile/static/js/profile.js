$(document).ready(function () {
  $(".pic-div-editable").hover(
    function () {
      $(this).css({ cursor: "pointer" });
    },
  );

  $(".pic-div-editable").click(function () {
    $("#change-dp-modal").modal("show");
  });

  var loadPostImage = function (event) {
    var image = document.getElementById("change-profile-image");
    image.src = URL.createObjectURL(event.target.files[0]);
  };

  $("#change-profile-image-file").on("change", function () {
    var $files = $(this).get(0).files;
    var image = $("#change-profile-image");
    image.attr("src", URL.createObjectURL($files[0]));
  });

  $("#change-profile-image-button").click(() => {
    var $files = $("#change-profile-image-file").get(0).files;

    if ($files.length) {
      // Reject big files
      if ($files[0].size > 1024 * 1024) {
        console.log("Please select a smaller file");
        alert("Please select an image of size less than 1 MB");
        return false;
      }
      // Begin file upload
      console.log("Uploading file to Imgur..");
      var apiUrl = "https://api.imgur.com/3/image";
      var apiKey = "b13f51ee210f02d";

      var settings = {
        // async: false,
        crossDomain: true,
        processData: false,
        contentType: false,
        type: "POST",
        url: apiUrl,
        headers: {
          Authorization: "Client-ID " + apiKey,
          Accept: "application/json",
        },
        mimeType: "multipart/form-data",
      };

      var formData = new FormData();
      formData.append("image", $files[0]);
      settings.data = formData;
      //   Response contains stringified JSON
      //   Image URL available at response.data.link
      $.ajax(settings).done(function (response) {
        response = JSON.parse(response);
        console.log(response.data.link);
        postImageUrl = response.data.link;

        // TODO Send New DP to Backend
      });
    }
  });

  $(".edit-bio").click(function () {
    $("#change-bio-modal").modal("show");
  });

  $("#change-bio-button").click(() => {
    var newBio = $("#change-bio-text").val();
    if (newBio.length == 0) {
      alert("No new bio provided");
    }
    // TODO Send New Bio to Backend
  });
});
