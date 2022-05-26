<template>
    <v-alert  class="account-error-list"
      dense
      outlined
      type="error"
    >
      <p v-for="(errors, field) in authError" :key="field">
         {{ field }}
        <ul>
          <li class="error-message" v-for="(error, idx) in errors" :key="idx">
            {{ error }}
          </li>
        </ul>
      </p>
    </v-alert>
  <!-- <div >
    <p v-for="(errors, field) in authError" :key="field">
      {{ field }}
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </li>
      </ul>
    </p>
  </div> -->
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style scoped>
 ul {
   list-style: none;
   display: flex;
 }
 p {
   margin-top: 4px;
   margin-bottom: 3px;
   margin-left: 0;
   font-family:'LeferiBaseType-RegularA';
   font-weight: 500;
  font-size: 12px;
 }
 li {
   margin-block-start: 0;
   padding: 0;
 }
.error-message {
    font-weight: 400;
    font-size: 12px;
 }
</style>
