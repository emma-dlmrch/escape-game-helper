import axios from 'axios';
import store from '@/store';

export async function imageUpload(file, gameId) {
    const formData = new FormData();

    formData.append('game', gameId);
    formData.append('image', file);
    formData.append('author', store.state.userId);
    try {
        const res = await axios.post('/upload-image/', formData);
        return '/' + res.data.image_relative_path;
    } catch (err) {
        console.error('Upload error:', err);

        if (err.response?.data?.non_field_errors) {
            alert(err.response.data.non_field_errors);
        } else if (err.response?.data?.image) {
            alert(err.response.data.image);
        } else {
            alert("Erreur lors de l'upload de l'image.");
        }

        throw err;
    }
}

export async function imageHandler(quill, gameId) {
    // On mémorise la position avant l'ouverture
    // du sélecteur de fichier.
    const range = quill.getSelection();

    const input = document.createElement('input');

    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');

    input.click();

    input.onchange = async () => {
        const file = input.files?.[0];

        if (!file) {
            return;
        }

        try {
            // Upload vers ton backend
            const url = await imageUpload(file, gameId);

            // Position d'insertion
            const index = range ? range.index : quill.getLength();

            // Insertion de l'image dans Quill
            quill.insertEmbed(index, 'image', url, 'user');

            // Curseur après l'image
            quill.setSelection(index + 1, 0, 'user');
        } catch (error) {
            console.error('Impossible d’insérer l’image:', error);
        }
    };
}
