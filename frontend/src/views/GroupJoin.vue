<template>

</template>

<script>
import Group from "@/objects/Group";
import RequestHandler from "@/utils/RequestHandler";

export default {
name: "JoinGroup",
  data: () => ({
    group: new Group(),
  }),
  mounted() {
    RequestHandler.getGroup(this.$route.params.id).then((response) => {
      this.group = response.data;
    });
  },
}
</script>

<style scoped>

</style>