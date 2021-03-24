
$( document ).ready(function() {
    $('.btn-explore').click(function() {
        $('.landing').fadeOut()
    })
});

var loadPostImage = function(event){
    var image = document.getElementById('post-image');
	image.src = URL.createObjectURL(event.target.files[0]);
}