import { loadQuill } from '@vueup/vue-quill'

let audioRegistered = false

export async function registerAudioBlot() {
    if (audioRegistered) {
        return
    }

    const Quill = await loadQuill()

    const BlockEmbed = Quill.import('blots/block/embed')

    class AudioBlot extends BlockEmbed {
        static blotName = 'audio'
        static tagName = 'audio'

        static create(url) {
            const node = super.create()

            node.setAttribute('src', url)
            node.setAttribute('controls', '')
            node.setAttribute('preload', 'metadata')

            return node
        }

        static value(node) {
            return node.getAttribute('src')
        }
    }

    Quill.register(AudioBlot)

    audioRegistered = true
}

export function audioHandler() {
    const url = window.prompt('URL du fichier audio')

    if (!url) return

    try {
        const parsedUrl = new URL(url)

        if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
            alert('URL non valide')
            return
        }
    } catch {
        alert('URL non valide')
        return
    }

    const range = this.quill.getSelection(true)

    this.quill.insertEmbed(
        range.index,
        'audio',
        url,
        'user'
    )

    this.quill.setSelection(range.index + 1, 0, 'user')
}