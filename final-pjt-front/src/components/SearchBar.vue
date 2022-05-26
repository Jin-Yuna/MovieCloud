<template>
<div>
  <v-row justify="center">
      <v-dialog
        v-model="dialog"
        max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="search" @click="setMoviesTitle()">
            <v-icon color="#1A2940" icon v-bind="attrs" v-on="on">mdi-magnify</v-icon> </v-btn>
        </template>
        <v-card>
          <v-card-title class="flex card-title">
            <span class="movie-search-title">영화 조회</span>
            <p class="explain">영화 검색 후 enter를 누르면 해당 영화로 안내됩니다</p>
          </v-card-title>
          <v-card-text>
            <form @submit.prevent="search()" class="mt-10">
              <v-autocomplete
                auto-select-first
                clearable
                v-model="result"
                :items="movies_title"
                item-text="title"
                item-value="pk"
                placeholder="찾는 영화를 검색해보세요"
              ></v-autocomplete>
            </form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="#1A2940"
              text
              @click="dialog = false"
              class="close">
              닫기
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      show: false,
      inputValue: '',
      result: null,
      result_show: false,
      dialog: false,
      movies_title: this.movieTitiles
    }
  },
  computed: {
    ...mapGetters(['movieSearchList', 'movieTitiles'])
  },
  mounted() {
    this.setMoviesTitle()
    console.log(this.movies_title)
  },
  methods: {
    toggleShow() {
      this.show = !this.show
      if (!this.show) {
        this.result = []
      }
    },
    search() {
      this.inputValue = this.result
      console.log('여기', this.inputValue)
      this.getMovieDetailAxios(this.inputValue)
      this.result = null
      this.dialog = false
      return
    },
    ...mapActions(['getMovieDetailAxios','setMoviesTitle']),
  }

}
</script>

<style>
.search {
  padding: 0;
  margin: 20px;
}
.movie-search-title {
  margin-top: 10px;
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 700;
  font-size: 30px;
  line-height: 46px;
  color: #1A2940;
  width:100%;
  text-align: center;
}
.close {
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 700;
  font-size: 30px;
}
.explain{
    width: 450px;
    margin: 0 auto;
    font-family: 'LeferiBaseType-RegularA';
    font-weight: 400;

    font-size: 18px;
    line-height: 129.49%;
    color: #1A2940;
    padding-top: 10px;
}
.card-title {
  align-items: center;
}
</style>