$(document).ready(() => {
    $('.post-like').click(function() {
        let id = $(this).attr('data-id')
        $.get('/like_post/' + id, (data) => {
            console.log(data)
            if(data == 1){
                likes = $('#post-likes-count'+id)
                likes.text(Number(likes.text())+1)
            }
        })
        return false
    })
})