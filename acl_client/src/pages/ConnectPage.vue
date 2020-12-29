<template>
  <div>
    <Header></Header>
    <el-card style="width:600px;margin:140px auto">
      <el-form ref="form" :model="connectData" label-width="80px" v-loading="loading">
        <h1 align="center">建立连接</h1>
          <el-form-item label="地址">
            <el-select v-model="connectData.address" placeholder="请选择地址">
              <el-option
                v-for="item in addressList"
                :key="item"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </el-form-item>
            <el-form-item label="用户名">
              <el-input v-model="connectData.username"></el-input>
          </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="connectData.password"></el-input>
          </el-form-item>
          <el-form-item >
              <el-button type="primary" round @click="handleConnect">连接</el-button>
          </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import Header from '@/components/Header'
export default {
  name: "ConnectPage",
  data() {
    return {
      loading:false,
      addressList:['192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.5'],
      connectData: {},
    };
  },
  components:{Header},
  methods: {
    handleConnect() {
      this.loading=true;
      this.$axios
        .post("/server/connect/", {
          connectData: this.connectData,
        })
        .then((res) => {
          this.loading=false;
          if (res.data.code === 200) {
            console.log(res);
            this.$message.success("连接成功!");
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
  },
};
</script>

<style scoped></style>
