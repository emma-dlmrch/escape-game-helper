import axios from 'axios';
import store from '@/store';

// export function imageHandler (file, gameId) {
//     return new Promise((resolve, reject) => {
//         const formData = new FormData();
//         formData.append("game", gameId);
//         formData.append("image", file);
//         formData.append("author", store.state.userId)

//         axios.post('/upload-image/', formData)
//             .then(res => {
//                 resolve("/"+res.data.image_relative_path);
//             })
//             .catch(err => {
//                 if (err.response.data.non_field_errors) {
//                     alert(err.response.data.non_field_errors)
//                 } else if (err.response.data.image) {
//                     alert(err.response.data.image)
//                 }
//                 reject("Upload failed");
//                 console.error("Error:", err)
//             })

//         }
//     )
// }

export function imageHandler(file, gameId) {
    return new Promise((resolve, reject) => {
        const formData = new FormData();

        formData.append("game", gameId);
        formData.append("image", file);
        formData.append("author", store.state.userId);

        axios.post('/upload-image/', formData)
            .then(res => {
                const url = "/" + res.data.image_relative_path;

                console.log("Image upload OK");
                console.log("URL retournée :", url);

                resolve(url);
            })
            .catch(err => {
                console.error("Upload error:", err);

                if (err.response?.data?.non_field_errors) {
                    alert(err.response.data.non_field_errors);
                } else if (err.response?.data?.image) {
                    alert(err.response.data.image);
                }

                reject(err);
            });
    });
}