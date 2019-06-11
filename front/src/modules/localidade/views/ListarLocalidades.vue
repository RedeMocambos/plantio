<template>
    <v-container fluid>
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <v-data-table
                    :headers="header"
                    :items="localidades"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="visualizar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    terrain
                                </v-icon>
                                {{ props.item.nome }}
                            </v-btn>
                        </td>
                        <td>{{ props.item.bioma }}</td>
                        <td>{{ props.item.clima }}</td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="editar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    edit
                                </v-icon>
                                editar
                            </v-btn>
                            <v-btn
                                flat
                                small
                                @click="excluir(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    clear
                                </v-icon>
                                excluir
                            </v-btn>
                        </td>
                    </template>
                </v-data-table>
                <v-btn
                    dark
                    class="green darken-1"
                    @click="adicionar()"
                >
                    <v-icon
                        white
                        class="pr-2">
                        add
                    </v-icon>
                    adicionar localidade
                </v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarLocalidades',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    align: 'center',
                    text: 'nome',
                    value: 'nome',
                },
                {
                    align: 'center',
                    text: 'bioma',
                    value: 'bioma',
                },
                {
                    align: 'center',
                    text: 'clima',
                    value: 'clima',
                },
                {
                    align: 'center',
                    text: 'ações',
                    value: 'acoes',
                },
            ],
            localidades: [],
        };
    },
    computed: {
        ...mapGetters({
            listaLocalidades: 'localidade/localidades',
        }),
    },
    watch: {
        listaLocalidades() {
            this.localidades = this.listaLocalidades;
        },
    },
    created() {
        this.buscarLocalidades();
    },
    methods: {
        ...mapActions({
            buscarLocalidades: 'localidade/buscarLocalidades',
            adicionarLocalidade: 'localidade/adicionarLocalidade',
        }),
        visualizar(id) {
            const path = `/localidade/${id}`;
            this.$router.push({ path });
        },
        editar(id) {
            const path = `/localidade/${id}/edit`;
            this.$router.push({ path });
        },
        adicionar() {
            this.adicionarLocalidade({
                nome: '',
                bioma: '',
                clima: '',
                cidade: '',
            }).then((response) => {
                this.editar(response.id);
            });
        },
        excluir(id) {
        },
    },
};
</script>
