const create = document.getElementById("create")
const postCreate = document.getElementById("create-post")
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
postUpload.addEventListener('change', () => {

    if(postUpload.files && postUpload.files[0]){
        console.log(postUpload.files, "postUpload")
        const url = URL.createObjectURL(postUpload.files[0]);
        postImage.src = url
        postImage.classList.remove('hidden')
    }

//     <div class="content flex items-center justify-center basis-1/2 relative p-2">
                    
//   <input type="file" name="" id="post-upload" class="hidden">
//   <label for="post-upload">
//     <div class="px-4 py-2 rounded-xl bg-blue-400  font-bold mt">Select from your computer</div>
//   </label>
// </div>

// <img id="imagePreview" style="display: none; position: absolute; top: 0; left: 0; z-index: 1;">

// <script>
// const displayImage = () => {
//   const input = document.getElementById("post-upload");
//   const preview = document.getElementById("imagePreview");

//   if (input.files && input.files[0]) {
//     const url = URL.createObjectURL(input.files[0]);

//     preview.src = url;
//     preview.style.display = "block";
//   }
// }

// document.getElementById("post-upload").addEventListener("change", displayImage);
// </script>

})
// function likePost () {
//    console.log(like.getAttribute("data-postId"))
//    // try{

//    // }catch(err){
//    //     console.oog(err)
//    // }
// }
// like.addEventListener('click', () => {
//     console.log("click")
// })
// likeButtons.forEach((like) => {
//     like.addEventListener("click", () => {
//         console.log(like, "like>>>>>>>")
//     })
// })