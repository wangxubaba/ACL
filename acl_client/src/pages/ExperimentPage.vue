<!--  -->
/* eslint-disable */
<template>
  <div>
    <Header></Header>
    <el-card style="margin:20px">
      <el-steps align-center :active="active" finish-status="success">
        <el-step
          title="实验1"
          description="配置 ospf 协议使得路由器可以连通，在这个地方我们通过在Router B上配置ACL禁止Router A到Router C的ospf流量通过，研究ACL如何控制路由更新的。"
        ></el-step>
        <el-step
          title="实验2"
          description="取消Router B设置的ACL来允许Router A到Router C的ospf数据包经过Router B"
        ></el-step>
        <el-step
          title="实验3"
          description="在Router B上设置ACL允许Router C发往Router A的ping以及响应数据通过，但是禁止Router A发往Router C的ping以及响应"
        ></el-step>
        <el-step
          title="实验4"
          description="在Router B设置ACL，禁止从Router A到Router C的telnet数据包经过，但是允许其它IP数据包经过，此时Router A可以ping通Router C，Router C可以telnet登录和ping通Router A"
        ></el-step>
        <el-step
          title="实验5"
          description="设置Router B为DNS服务器，Router A使用Router B的DNS服务，我们通过在Router B设置ACL的方式，研究ACL如何阻断DNS流量"
        ></el-step>
      </el-steps>
      <el-button
        type="primary"
        round
        style="margin-top: 12px;"
        @click="previous"
        >上一步</el-button
      >
      <el-button type="primary" round style="margin-top: 12px;" @click="next"
        >下一步</el-button
      >
    </el-card>

    <el-card style="margin:20px" v-if="step[0] == true">
      <el-row>
        <el-col :span="8">
          <div class="grid-content bg-purple">
            <h3>配置Router A</h3>
            <code
              >en<br />
              conf t<br />
              router ospf 1<br />
              network 192.168.12.0 0.0.0.255 a 0<br />
              network 192.168.0.0 0.0.0.255 a 0<br />
            </code>
          </div>
        </el-col>
        <el-col :span="8"
          ><div class="grid-content bg-purple-light">
            <h3>配置Router B</h3>
            <code
              >en<br />
              conf t<br />
              access-list 100 deny ospf any any <br />
              access-list 100 permit ip any any<br />
              int s2/0<br />
              ip access-group 100 in<br />
              router ospf 1<br />
              network 192.168.12.0 0.0.0.255 a 0<br />
              network 192.168.23.0 0.0.0.255 a 0<br />
              network 192.168.0.0 0.0.0.255 a 0<br />
            </code></div
        ></el-col>
        <el-col :span="8">
          <div class="grid-content bg-purple">
            <h3>配置Router C</h3>
            <code
              >en<br />
              conf t<br />
              router ospf 1<br />
              network 192.168.23.0 0.0.0.255 a 0<br />
              network 192.168.0.0 0.0.0.255 a 0<br />
            </code></div
        ></el-col>
      </el-row>
      <el-divider></el-divider>
      <el-row>
        <el-col :span="12"
          ><div class="grid-content bg-purple">
            <h3>验证Router A</h3>
            <code>p 192.168.23.3<br /> </code></div
        ></el-col>
        <el-col :span="12"
          ><div class="grid-content bg-purple-light">
            <h3>验证Router C</h3>
            <code>p 192.168.12.1<br /> </code></div
        ></el-col>
      </el-row>
      <el-button type="primary" round @click="handle0">配置并验证</el-button>
    </el-card>
    <el-card style="margin:20px" v-if="step[1] == true">
      <div>
        <h3>配置Router B</h3>
        <code
          >en<br />
          conf t<br />
          int s2/0<br />
          no ip access-group 100 in<br />
        </code>
       
        <el-divider></el-divider>
        <el-row>
          <el-col :span="12"
            ><div class="grid-content bg-purple">
              <h3>验证Router A</h3>
              <code>p 192.168.23.3<br /> </code></div
          ></el-col>
          <el-col :span="12"
            ><div class="grid-content bg-purple-light">
              <h3>验证Router C</h3>
              <code>p 192.168.12.1<br /> </code></div
          ></el-col>
        </el-row>
         <el-button type="primary" round @click="handle1">配置并验证</el-button>
      </div>
    </el-card>
    <el-card style="margin:20px" v-if="step[2] == true">
      <div>
        <h3>配置Router B</h3>
        <code
          >en<br />
          conf t<br />
          access-list 101 permit icmp any any echo-reply <br />
          int s2/0<br />
          ip access-group 101 in<br />
        </code>

        <el-divider></el-divider>
        <el-row>
          <el-col :span="12"
            ><div class="grid-content bg-purple">
              <h3>验证Router A</h3>
              <code>p 192.168.23.3<br /> </code></div
          ></el-col>
          <el-col :span="12"
            ><div class="grid-content bg-purple-light">
              <h3>验证Router C</h3>
              <code>p 192.168.12.1<br /> </code></div
          ></el-col>
        </el-row>
        <el-button type="primary" round @click="handle2">配置并验证</el-button>
      </div>
    </el-card>
    <el-card style="margin:20px" v-if="step[3] == true">
      <div>
        <h3>恢复Router B的ACL配置</h3>
        <code
          ># Router B<br />
          # telnet 192.168.0.4<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#int s2/0<br />
          Router(config-if)#no ip access-group 101 in<br />
          Router(config-if)#end<br />
          Router#ex<br />
        </code>
        <h3>配置Router B</h3>
        <code
          ># Router B的s2/0上设置ACL<br />
          # telnet 192.168.0.4<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#access-list 102 deny tcp any any eq telnet<br />
          Router(config)#access-list 102 permit ip any any <br />
          Router(config)#int s2/0<br />
          Router(config-if)#ip access-group 102 in<br />
          Router(config-if)#end<br />
          Router#ex<br />
        </code>
        <el-divider></el-divider>
        <el-row>
          <el-col :span="12"
            ><div class="grid-content bg-purple">
              <h3>验证Router A</h3>
              <code
                ># Router A<br />
                # telnet 192.168.0.3<br />
                # enter password: CISCO<br />
                # ping Router C，应该ping通<br />
                Router>p 192.168.23.3<br />
                # telnet Router C，应该因为超时（7s）被拒绝<br />
                Router>telnet 192.168.23.3<br />
              </code></div
          ></el-col>
          <el-col :span="12"
            ><div class="grid-content bg-purple-light">
              <h3>验证Router C</h3>
              <code>
                # Router C<br />
                # telnet 192.168.0.5<br />
                # enter password: CISCO<br />
                # ping Router A，应该ping通<br />
                Router>p 192.168.12.1<br />
                # telnet Router A，应该可以正常登录<br />
                Router>telnet 192.168.12.1<br />
                # enter password: CISCO<br />
                Router>ex #此步骤结束后退出到Router C<br />
                Router>ex<br />
              </code></div
          ></el-col>
        </el-row>
        <el-button type="primary" round @click="handle3">配置并验证</el-button>
      </div>
    </el-card>
    <el-card style="margin:20px" v-if="step[4] == true">
      <div>
        <h3>恢复Router B的ACL配置</h3>
        <code
          ># Router B<br />
          # telnet 192.168.0.4<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#int s2/0<br />
          Router(config-if)#no ip access-group 102 in<br />
          Router(config-if)#end<br />
          Router#ex<br />
        </code>
        <h3>配置RouterB</h3>
        <code>
          # Router B的s2/0上设置ACL<br />
          # telnet 192.168.0.4<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#ip dns server<br />
          Router(config)#ip domain lookup <br />
          Router(config)#ip host router_c 192.168.23.3<br />
          Router(config)#access-list 103 deny udp any any eq domain<br />
          Router(config)#access-list 103 permit ip any any<br />
          Router(config)#int s2/0<br />
          Router(config-if)#ip access-group 103 in<br />
          Router(config-if)#end<br />
          Router#ex<br />
        </code>
        <el-divider></el-divider>
        <h3>验证RouterA</h3>
        <code>
          # Router A<br />
          # telnet 192.168.0.3<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#ip domain lookup<br />
          Router(config)#ip name-server 192.168.0.4<br />
          Router(config)#end<br />
          # Router A会向Router B询问router_c对应的IP地址<br />
          # 但是我们设置ACL不允许dns流量通过，因此这一步不能成功<br />
          Router#p router_c<br />
          Router#ex<br />
        </code>
        <el-button type="primary" round @click="handle4">配置并验证</el-button>
        <el-divider></el-divider>
        <h3>恢复RouterB</h3>
        <code>
          # Router B<br />
          # telnet 192.168.0.4<br />
          # enter password: CISCO<br />
          Router>en<br />
          # enter password: CISCO<br />
          Router#conf t<br />
          Router(config)#int s2/0<br />
          Router(config-if)#no ip access-group 103 in<br />
          Router(config-if)#end<br />
          Router#ex<br />
        </code>
        <el-divider></el-divider>
        <h3>验证RouterA</h3>
        <code>
          # telnet 192.168.0.3<br />
          # enter password: CISCO<br />
          # Router A会向Router B询问router_c对应的IP地址，这一步成功<br />
          Router>p router_c<br />
          Router>ex<br />
        </code>
        <el-button type="primary" round @click="handle5">配置并验证</el-button>
      </div>
    </el-card>

    <!-- <div class="experimentList">
      <el-card
        class="exper"
        v-for="(exp, index) in experimentsList"
        :key="index"
      >
        <div style="text-align:center">
          <img src="@/assets/logo.png" @ />
          <h3>{{exp}}</h3>
        </div>
      </el-card>
    </div>-->
  </div>
</template>

<script>
import Header from "@/components/Header";
export default {
  components: { Header },
  data() {
    return {
      step: [true, false, false, false, false],
      active: 0,
    };
  },
  methods: {
    previous() {
      if (this.active != 0) {
        this.step[this.active] = false;
        this.step[this.active - 1] = true;
        this.active--;
      }
    },
    next() {
      if (this.active == 4) {
        this.active = 0;
        this.step[4] = false;
        this.step[0] = true;
      } else {
        this.step[this.active] = false;
        this.step[this.active + 1] = true;
        this.active++;
      }
    },
    handle0() {
      this.$axios
        .post("/server/execute/script/", {
          id: 0,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            console.log(res);
            this.$message.success(res.data.msg);
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
    handle1() {
      this.$axios
        .post("/server/execute/script/", {
          id: 1,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            this.$message.success(res.data.msg);
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
    handle2() {
      this.$axios
        .post("/server/execute/script/", {
          id: 2,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            this.$message.success(res.data.msg);
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
    handle3() {
      this.$axios
        .post("/server/execute/script/", {
          id: 3,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            this.$message.success(res.data.msg);
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
    handle4() {
      this.$axios
        .post("/server/execute/script/", {
          id: 4,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            this.$message.success("连接成功!");
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
    handle5() {
      this.$axios
        .post("/server/execute/script/", {
          id: 5,
        })
        .then((res) => {
          this.loading = false;
          if (res.data.code === 200) {
            this.$message.success(res.data.msg);
          } else {
            this.$message.error(res.data.msg);
          }
        });
    },
  },
};
</script>
<style scoped>

</style>
