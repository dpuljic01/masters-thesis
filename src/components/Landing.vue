<template>
  <div id="landing" class="dp-bg1">
    <md-empty-state
      class="md-primary"
      md-icon="attach_money"
      md-label="Financial Dashboard"
      md-description="Evaluate and analyze your investment portfolio,
      keep track of your earnings and use our tools for smarter future investments."
    >
      <router-link to="/register">
        <md-button class="md-primary md-raised">Create account</md-button>
      </router-link>
      <br><span flex>Already a member?</span>
      <router-link to="/login">
        <md-button class="md-secondary md-raised">Log in</md-button>
      </router-link>
    </md-empty-state>
  </div>
</template>

<script>
export default {
  name: 'Landing',
};
</script>

<style scoped>
#landing {
  background-size: cover;
  min-height: 100vh;
}
</style>
