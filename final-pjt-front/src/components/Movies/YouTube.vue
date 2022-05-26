<template>
  <div>
    <iframe
      width="1280"
      height="720"
      :src="`https://www.youtube.com/embed/${selectedVideo.id.videoId}`"
      frameborder="0">
    </iframe>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: {
    movietitle: String,
  },
  data() {
    return {
      video: null,
      selectedVideo: null,
    }
  },
  methods: {
    getVideo() {
      // 요청
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const config = {
        params: {
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.movietitle + '공식예고편'
        }
      }

      axios.get(API_URL, config)
        .then(response => {
          console.log('요청', response)
          this.selectedVideo = response.data.items[0]
        })
        .catch(err=>{console.log(err)})
    },
  },
  mounted() {
    this.getVideo()
  }
}
</script>

<style>

</style>