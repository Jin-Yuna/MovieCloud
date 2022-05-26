<template>
  <div>
    <form @submit.prevent="onSubmit" class="form">
      <!-- 수정할 때는 영화목록 선택 안보이게 함 -->
      <div v-if="this.action==='create'"> 
        <label for="movie">영화</label>
        <input type="text" @click="toggleShow" :placeholder="this.result_movie">
        <!-- <select id="movie" v-model="newDrop.movie">
          <option v-for="movie_title in movies_title" :value="movie_title.pk" :key="movie_title.pk">
            <span>{{ movie_title.title }}</span>
          </option>
        </select> -->
      </div>
      <!-- 별점 -->
      <div class="myrate_potition">
        <div id="myrate">
          <fieldset>
              <input type="radio" v-model="newDrop.user_vote" name="rating" value="5" id="rate1"><label for="rate1">⭐</label>
              <input type="radio" v-model="newDrop.user_vote" name="rating" value="4" id="rate2"><label for="rate2">⭐</label>
              <input type="radio" v-model="newDrop.user_vote" name="rating" value="3" id="rate3"><label for="rate3">⭐</label>
              <input type="radio" v-model="newDrop.user_vote" name="rating" value="2" id="rate4"><label for="rate4">⭐</label>
              <input type="radio" v-model="newDrop.user_vote" name="rating" value="1" id="rate5"><label for="rate5">⭐</label>
            <span>평점</span>    
          </fieldset>
        </div>
      </div>
      <!--  -->
      <div>
        <label for="title">한줄평</label>
        <input type="text" id="title" v-model="newDrop.title">
      </div>
      <div class="mt-4">
        <label for="content">내용</label>
        <textarea id="content" cols="30" rows="10" v-model="newDrop.content"></textarea>
      </div>
      <!-- <div>
        <label class="form-label" for="user_vote">평점</label>
        <input class="form-control" type="number" id="user_vote" min="0" max="5" step="1" v-model="newDrop.user_vote">
      </div> -->
      <button class="my_btn">생    성    하   기</button>
    </form>
    <!-- 모달  -->
    <div>
      <transition>
        <div id="search" class="modal" v-if="this.show">
          <div class="bg"></div>
            <div class="searchbar">
              <div class="flex explain">
                <p>영화를 검색해보아용</p>
                <button @click="toggleShow">닫기</button>
              </div>
              <input type="text" @keyup.enter="search">
              <div v-if="result_show">
                <li
                  v-for="result_movie in result"
                  :key="result_movie.pk"
                  @click="setMovieId(result_movie.pk, result_movie.title)">
                  {{ result_movie.title }}
              </li>
            </div>
          </div>
        </div>
      </transition>
    </div>  
  </div>

  


</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'DropCreate',
  props: {
    drop: Object,
    action: String,
    movies_title : Array,
  },
  data() {
    return {
      newDrop: {
        title: this.drop.title,
        content: this.drop.content,
        movie: this.drop.movie_id, // 영화 아이디(pk)
        user_vote: this.drop.user_vote,
        movies_title : this.$store.state.movies.movies_title
      },
      movietitle : null,
      show: false,
      inputValue: '',
      result: [],
      result_show: false,
      result_movie: ''
    }
  },

  methods: {
    ...mapActions(['createDrop', 'updateDrop']),
    onSubmit() {
      if (this.action === 'create') {
        this.createDrop(this.newDrop)
      } else if (this.action === 'update') {
        const payload = {
          dropPk: this.drop.id,
          ...this.newDrop,
        }
        this.updateDrop(payload)
      }
    },
    setMovieId(movieid, movietitle) {
      this.newDrop.movie = movieid
      this.result_movie = movietitle
    }, 
    toggleShow() {
      this.show = !this.show
      if (!this.show) {
        this.result = []
      }
    },
    search(event) {
      this.inputValue = event.target.value
      const movies = this.movies_title
      for (var movie of movies) {
        if (movie.title.includes(this.inputValue)) {
          this.result.push(movie)
        }
      }
      this.result_show = true
    },
  }
}
</script>

<style scoped>
label {
  font-family: 'LeferiBaseType-RegularA';
  color: #425E7A;
}
input {
  font-family: 'LeferiPoint-WhiteObliqueA';
  color: #425E7A;
}
textarea {
  font-family: 'LeferiPoint-WhiteObliqueA';
  color: #425E7A;  
}

.my_btn {
  position: absolute;
  margin-top: 6rem;
  width: 81rem;
  height: 52px;
  background: #425E7A;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;

  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 129.49%;
  align-items: center;
  text-align: center;
  color: #F7F8FB;
}



/* 모달 */
.v-enter-active, .v-leave-active {
  transition: opacity 1s;
}
/* 더 이상 보이게 되지 않았을 때의 투명도 */
.v-enter, .v-leave-to {
  opacity: 0;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal .bg {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
        }
.searchbar {
  position: absolute;
  background-color: #fff;
  width: 400px;
  height: 300px;
  padding: 15px;
        }
.explain {
  align-items: center;
  justify-content: space-between;
}

/* 별점 */
#myrate fieldset{
  display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
  direction: rtl; /* 이모지 순서 반전 */
  border: 0; /* 필드셋 테두리 제거 */
}
#myrate input[type=radio]{
  display: none; /* 라디오박스 감춤 */
}
#myrate label{
  font-size: 1em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #c6dced; /* 새 이모지 색상 부여 */
}
#myrate label:hover{
  text-shadow: 0 0 0 rgb(89, 108, 216); /* 마우스 호버 */
}
#myrate label:hover ~ label{
  text-shadow: 0 0 0 rgb(89, 108, 216); /* 마우스 호버 뒤에오는 이모지들 */
}
#myrate fieldset legend{
  text-align: left;
}
#myrate input[type=radio]:checked ~ label{
  text-shadow: 0 0 0 rgb(89, 108, 216); /* 마우스 클릭 체크 */
}
.myrate_potition {
  position: relative;
  top: -2rem;
  left: 71rem;
}
/* 택스트 효과 */

</style>