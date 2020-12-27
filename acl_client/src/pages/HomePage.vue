<!--  -->
/* eslint-disable */
<template>
  <div>
    <Menu mode="horizontal" :theme="theme" active-name="1">
      <MenuItem name="1">
        <Icon type="ios-paper" />
        实验内容
      </MenuItem>
      <MenuItem name="2">
        <Icon type="ios-people" />
        登录配置
      </MenuItem>
      <MenuItem name="4">
        <Icon type="ios-construct" />
        验证
      </MenuItem>
    </Menu>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      theme: light
    };
  },
  methods: {},
};
</script>
<style scoped></style>
