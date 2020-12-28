<!--  -->
/* eslint-disable */
<template>
  <div>
    <Header></Header>
    <div class="experimentList">
      <Card v-for="(exp,index) in experimentsList" :key="index" style="width:300px">
        <div style="text-align:center">
          <img src="@/assets/logo.png" />
          <h3>A high quality UI Toolkit based on Vue.js</h3>
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
export default {
  components: { Header },
  data() {
    return {
      experimentsList: [1, 2, 3],
    };
  },
  methods: {},
};
</script>
<style scoped>
.experimentlist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
