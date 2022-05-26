<template>
  <div>
    <form @submit.prevent="onSubmit" class="mt-10">
      <!-- 수정할 때는 영화목록 선택 안보이게 함 -->
      <div v-if="this.action==='create'"> 
        <v-autocomplete
          solo
          v-model="newDrop.movie"
          :items="movies_title"
          item-text="title"
          item-value="pk"
          placeholder="리뷰할 영화를 선택하세요"
        >
        </v-autocomplete>
      </div>
      <div>
        <v-text-field
          label="제목"
          outlined
          v-model="newDrop.title"
          :rules="rules"
          hide-details="auto"
        ></v-text-field>
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
      </div>
      <div class="mt-5">
        <v-textarea
          outlined
          label="내용"
          v-model="newDrop.content"
        ></v-textarea>
      </div>
      <v-btn block large color="blue-grey" class="my_btn" @click="onSubmit">생    성    하   기</v-btn>
    </form>
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
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
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
  },
  created(){
  }
}
</script>

<style scoped>
.myfont {
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
  background: #425E7A;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;

  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 129.49%;
  color: #F7F8FB;
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
  position: absolute;
  left: calc(50% + 179px/2 + 600px);
  top: calc(50% - 26px/2 - 370px);
}
/* 택스트 효과 */

</style>