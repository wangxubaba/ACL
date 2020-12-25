<template>
    <div>
        <p>这里是telnet远程连接的页面</p>
        <Button type="primary" @click="test">{{test_text}}</Button>
    </div>
</template>

<script>
    export default {
        name: "ConnectPage",
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