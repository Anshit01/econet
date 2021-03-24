let postImageUrl = ''


$( document ).ready(function() {
    $('.btn-explore').click(function() {
        $('.landing').fadeOut()
    })

    $('input[type=file]').on('change', function () {
        let postImageStatus = $('.post-image-status')
        postImageStatus.text('')
        postImageUrl = ''
        var $files = $(this).get(0).files;
        console.log('Got file')
        if ($files.length) {
            // Reject big files
            if ($files[0].size > 1024 * 1024) {
                console.log('Please select a smaller file');
                alert('Please select an image of size less than 1 MB')
                return false;
            }

            var image = document.getElementById('post-image');
	        image.src = URL.createObjectURL($files[0]);

            // Begin file upload
            console.log('Uploading file to Imgur..');
            postImageStatus.text('Uploading image....')
            var apiUrl = 'https://api.imgur.com/3/image';
            var apiKey = 'b13f51ee210f02d';
        
            var settings = {
                // async: false,
                crossDomain: true,
                processData: false,
                contentType: false,
                type: 'POST',
                url: apiUrl,
                headers: {
                Authorization: 'Client-ID ' + apiKey,
                Accept: 'application/json',
                },
                mimeType: 'multipart/form-data',
            };
        
            var formData = new FormData();
            formData.append('image', $files[0]);
            settings.data = formData;
        
            // Response contains stringified JSON
            // Image URL available at response.data.link
            $.ajax(settings).done(function (response) {
                response = JSON.parse(response)
                console.log(response.data.link)
                postImageUrl = response.data.link
                postImageStatus.text('Image Uploaded.')
            });
        }
    });


});

var loadPostImage = function(event){
    var image = document.getElementById('post-image');
	image.src = URL.createObjectURL(event.target.files[0]);
}

