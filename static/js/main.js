const create = document.getElementById("create")
const postCreate = document.getElementById("create-post")
//const viewPost = document.getElementById("view-post")
//const postModal = document.getElementById("post-modal")
// const posts = document.querySelectorAll("#post")
const postUpload = document.getElementById("post-upload")
const postImage = document.getElementById("post-img")
// const myForm = document.getElementById("comment-form")
// //const comment = document.getElementById("comment")


// myForm.addEventListener('submit', (e) => {
//     e.preventDefault()
//     console.log("hello")
// })
    
// })

// posts.forEach((post) => {
//     post.getElementById("addComment").addEventListener("submit", (e) =>{
//         e.preventDefault()
//         console.log("hello")
//     })
// })
   
// viewPost.addEventListener('click', () => {
//     console.log("viewPost")
//     // postModal.classList.toggle('hidden');
// })

create.addEventListener('click', () => {
    console.log(postCreate);
    postCreate.classList.toggle('hidden');
    console.log("remove")
})
window.onclick = function(event) {
    if (event.target == postCreate) {
        postCreate.classList.toggle('hidden');
    }
}
postUpload?.addEventListener('change', () => {

    if(postUpload.files && postUpload.files[0]){
        console.log(postUpload.files, "postUpload")
        const url = URL.createObjectURL(postUpload.files[0]);
        postImage.src = url
        postImage.classList.remove('hidden')
    }

})
