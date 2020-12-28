<template>
  <div>
    <Header></Header>
    <Card style="width:600px;margin:140px auto">
      <Form :model="connectData" :label-width="50">
        <h1 align="center">建立连接</h1>
        <FormItem label="地址">
          <Select v-model="connectData.address">
            <Option
              v-for="add in addressList"
              :value="add"
              :key="add"
              >{{ add }}</Option
            >
          </Select>
        </FormItem>
        <FormItem label="用户">
          <Input
            v-model="connectData.username"
            placeholder="请输入用户"
          ></Input>
        </FormItem>
        <FormItem label="密码">
          <Input
            v-model="connectData.password"
            placeholder="请输入密码"
          ></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="handleConnect">连接</Button>
        </FormItem>
      </Form>
      <Spin size="large" fix v-if="spinShow"></Spin>
    </Card>
  </div>
</template>

<script>
import Header from '@/components/Header'
export default {
  name: "ConnectPage",
  data() {
    return {
      spinShow:false,
      addressList:['192.168.1.1','192.168.1.2','192.168.1.3'],
      connectData: {},
    };
  },
  components:{Header},
  methods: {
    handleConnect() {
      this.spinShow=true;
      this.$axios
        .post("/server/connect/", {
          connectData: this.connectData,
        })
        .then((res) => {
          this.spinShow=false;
          if (res.data.code === 200) {
            console.log(res);
            this.$Message.success("连接成功!");
          } else {
            this.$Message.error(res.data.msg);
          }
        });
    },
  },
};
</script>

<style scoped></style>
