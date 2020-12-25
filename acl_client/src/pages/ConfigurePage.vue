<template>
    <div>
        <p>这里是配置页面，包括命令顺序调换，打开、保存、新建、删除、执行、验证</p>
        <Button type="primary" @click="test">{{test_text}}</Button>
    </div>
</template>

<script>
    export default {
        name: "ConfigurePage",
        data(){
          return{
              test_text:'TEST'
          }
        },
        methods:{
            test(){
                this.$axios.post('/server/test_connection/',{test:'111'}).then(re=>{
                    console.log(re)
                })
            }
        }
    }
</script>

<style scoped>

</style>